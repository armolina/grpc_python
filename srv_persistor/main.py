import grpc
import sales_record_pb2
import sales_record_pb2_grpc
import json

from concurrent import futures
from repository.mongodb_repository import MongodbRepository

class SalesRecord(sales_record_pb2_grpc.SalesRecordServicer):
    def PingSalesRecords(self, request, context):
        return sales_record_pb2.SalesRecordPingResponse(result="1")
    
    def SendSalesRecords(self, request, context):
        rec_item = {
            "region":request.region,
            "item_type":request.item_type,
            "units_sold":request.units_sold,
            "units_price":request.unit_price,
            "units_cost":request.unit_cost
        }

        mongoClient = MongodbRepository("root", "example", "mongo:27017")
        result=mongoClient.insert_one(rec_item, "sales_records")
        return sales_record_pb2.SalesRecordResponse(data=result.inserted_id)

    def SendSalesRecordsStream(self, request_iterator, context):
        for request in request_iterator:
            print(request.country)
        return sales_record_pb2.SalesRecordResponse(data="1")

    def SendSalesPayload(self, request, context):
        obj = json.loads(request.payload)
        print(type(obj))
        mongoClient = MongodbRepository("root", "example", "mongo:27017")
        result=mongoClient.insert_many(obj, "sales_records")
        return result

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))

    sales_record_pb2_grpc.add_SalesRecordServicer_to_server(SalesRecord(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("server started, port: 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    main()