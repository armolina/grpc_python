.PHONY = pb2

SHELL := /bin/bash

VENV = env
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

pb2:
	python3 -m venv env
	$(PIP) install grpcio grpcio-tools
	$(PYTHON) -m grpc_tools.protoc -I protobufs --python_out=srv_persistor/ --grpc_python_out=srv_persistor/ protobufs/sales_record.proto

	cp -R srv_persistor/sales_record_pb2.py srv_reader
	cp -R srv_persistor/sales_record_pb2_grpc.py srv_reader

	rm -r $(VENV)

local_env:
	python3 -m venv srv_reader/env
	srv_reader/$(PIP) install --upgrade pip
	srv_reader/$(PIP) install -r srv_reader/requirements.txt

	python3 -m venv srv_persistor/env
	srv_persistor/$(PIP) install --upgrade pip
	srv_persistor/$(PIP) install -r srv_reader/requirements.txt