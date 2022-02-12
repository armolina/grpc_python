import sys
import csv
import grpc

import managers_pb2_grpc
import managers_pb2

def main():
    f = open("/tmp/data/Managers.csv")
    dataReader = csv.reader(f, delimiter=',')

    with grpc.insecure_channel('srv_persistor:50051') as channel:
        stub = managers_pb2_grpc.ManagerStub(channel)
        response = stub.PingManagers(managers_pb2.EmptyMesssage())
    print("Mensaje recibido: " + response.result)

    print("Service finish!")

if __name__ == "__main__":
    main()