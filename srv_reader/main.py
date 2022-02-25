import sys
import csv
import grpc

from repository.file_repository import FileRepository
from dto.sales_record import SaleRecord

import managers_pb2_grpc
import managers_pb2

def main():

    file_repository = FileRepository("./srv_reader/small_sales_records.csv")
    data_readed = file_repository.read_data()

    sales_records = []

    for row in data_readed:
        sale_record = SaleRecord(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
        sales_records.append(sale_record)

        with grpc.insecure_channel('srv_persistor:50051') as channel:
            stub = managers_pb2_grpc.(channel)
            response = stub.PingManagers(managers_pb2.EmptyMesssage())
            print("Mensaje recibido: " + response.result)
    
    channel.close()
    print("Service finish!")

if __name__ == "__main__":
    main()