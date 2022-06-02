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

    conn_mode = os.environ["CONNECTION_MODE"]
    start_time = time.time()

    if(conn_mode=="0"):
        print("Ping start!") 
        payload_connection(data_readed)
        print("Ping finish!") 
    elif(conn_mode=="1"):
        print("Service unary start!")  
        unary_connection(data_readed)
        print("Service unary finish!")  
    elif(conn_mode=="2"):
        print("Service stream start!")  
        stream_connection(data_readed)
        print("Service stream finish!")
    
    end_time = time.time()
    print("elapsed time: " + str(end_time-start_time))

def payload_connection(data_readed):   
    with grpc.insecure_channel('srv_persistor:50051') as channel:
        stub = sales_record_pb2_grpc.SalesRecordStub(channel)
        request = sales_record_pb2.PayloadRequest(payload=str(data_readed))
        result = stub.SendSalesPayload(request)
        print(f'result:{result.data}')

def unary_connection(data_readed):
    for row in data_readed:
        with grpc.insecure_channel('srv_persistor:50051') as channel:
            stub = sales_record_pb2_grpc.SalesRecordStub(channel)
            message = make_message(row)
            result=stub.SendSalesRecords(message)
            print(f'result:{result.data}')
        channel.close()

def stream_connection(data_readed):
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
    print(os.environ["HOSTNAME"])
    return sales_record_pb2.SalesRecordRequest(
        region=message[0],
        item_type=message[2],
        units_sold=message[8],
        unit_price=message[9],
        unit_cost=message[10],
        source=os.environ["HOSTNAME"]
    )

if __name__ == "__main__":
    main()