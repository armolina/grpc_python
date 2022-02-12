import sys
import csv
import grpc
import managers_pb2
import managers_pb2_grpc

from concurrent import futures

class Manager(managers_pb2_grpc.ManagerServicer):
    def PingManagers(self, request, context):
        return managers_pb2.ManagerPingResponse(result="1")
    

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    managers_pb2_grpc.add_ManagerServicer_to_server(Manager(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("server started, port: 50051")
    server.wait_for_termination()

    print("Service finish!")

if __name__ == "__main__":
    main()