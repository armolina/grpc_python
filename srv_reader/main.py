import os
import grpc
import time

from repository.file_repository import FileRepository
from dto.sales_record import SaleRecord

import sales_record_pb2
import sales_record_pb2_grpc

def main():
    file_repository = FileRepository(os.environ["DIR_FILE"])
    data_readed = file_repository.read_data()

    start_time = time.time()
    sales_records = []
    iteration = 0

    for row in data_readed:
        sale_record = SaleRecord(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
        sales_records.append(sale_record)

        with grpc.insecure_channel('srv_persistor:50051') as channel:
            stub = sales_record_pb2_grpc.SalesRecordStub(channel)
            request = sales_record_pb2.SalesRecordRequest(region=row[0])
            response = stub.SendSalesRecords(request)
        
        print("Iteracion: " + str(iteration) + "/5000000")
        iteration += 1

    end_time = time.time()
    print(start_time-end_time)
    
    channel.close()
    print("Service finish!")

if __name__ == "__main__":
    
    main()
