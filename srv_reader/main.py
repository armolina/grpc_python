from ctypes import sizeof
import os
import grpc
import time
import json

from repository.file_repository import FileRepository
from dto.sales_record import SaleRecord

import sales_record_pb2
import sales_record_pb2_grpc

def main():
    file_repository = FileRepository(os.environ["DIR_FILE"])
    data_readed = file_repository.read_data()
    
    payload_connection(data_readed)
    
    """
    print("Service unary start!")  
    start_time = time.time()
    unary_connection(data_readed)
    end_time = time.time()
    print(start_time-end_time)
    print("Service unary finish!")

    print("Service stream start!")  
    start_time = time.time()
    stream_connection(data_readed)
    end_time = time.time()
    print(start_time-end_time)
    print("Service stream finish!")
    """

def payload_connection(data_readed):
    sales_records = []
    
    for row in data_readed:
        sale_record = SaleRecord(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
        sales_records.append(sale_record)
    
    with grpc.insecure_channel('srv_persistor:50051') as channel:
        stub = sales_record_pb2_grpc.SalesRecordStub(channel)
        request = sales_record_pb2.PayloadRequest(payload=json.dumps(sales_records))
        stub.SendSalesPayload(request)
    

def unary_connection(data_readed):
    iteration = 0
    sales_records = []
    
    for row in data_readed:
        sale_record = SaleRecord(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
        sales_records.append(sale_record)

        with grpc.insecure_channel('srv_persistor:50051') as channel:
            stub = sales_record_pb2_grpc.SalesRecordStub(channel)
            request = sales_record_pb2.SalesRecordRequest(region=row[0])
            response = stub.SendSalesRecords(request)
        channel.close()
        iteration += 1


def stream_connection(data_readed):

    
    #for row in data_readed:
    #    sales_records.append(make_message(row))

    with grpc.insecure_channel('srv_persistor:50051') as channel:
        stub = sales_record_pb2_grpc.SalesRecordStub(channel)
        response = stub.SendSalesRecordsStream(generate_messages(data_readed))
        print(response)

def generate_messages(data_readed):
    messages=[]

    for data in data_readed:
        messages.append(make_message(data))

    for msg in messages:
        yield msg

def make_message(message):
    return sales_record_pb2.SalesRecordRequest(
        region=message[0],
        country=message[1],
        item_type=message[2],
        sales_channel=message[3],
        order_priority=message[4],
        order_date=message[5],
        order_id=message[6],
        ship_date=message[7],
        units_sold=message[8],
        unit_price=message[9],
        unit_cost=message[10],
        total_revenue=message[11],
        total_cost=message[12],
        total_profit=message[13]
    )


if __name__ == "__main__":
    main()
