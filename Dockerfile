FROM python:2.7
RUN apt-get update && apt-get install -y unzip
ADD . /kv
WORKDIR /kv
RUN ./script/install-protoc
RUN pip install grpcio
RUN ./script/install-grpc
RUN ./script/generate
