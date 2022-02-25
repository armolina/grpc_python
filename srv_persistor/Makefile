.PHONY = pb2

SHELL := /bin/bash

pb2:
	python3 -m venv make_env
	source make_env/bin/activate
	pip3 install -r requirements.txt
	python3 -m grpc_tools.protoc -I protobufs --python_out=. --grpc_python_out=. protobufs/managers.proto

	rm -r make_env