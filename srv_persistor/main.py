import sys
import csv
import grpc
import sales_record_pb2
import sales_record_pb2_grpc

from concurrent import futures

class SalesRecord(sales_record_pb2_grpc.SalesRecordServicer):
    def PingSalesRecords(self, request, context):
        return sales_record_pb2.SalesRecordPingResponse(result="1")
    

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    sales_record_pb2_grpc.add_SalesRecordServicer_to_server(SalesRecord(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("server started, port: 50051")
    server.wait_for_termination()

    print("Service finish!")

if __name__ == "__main__":
    main()