FROM python:2.7
ADD . /kv
WORKDIR /kv
RUN pip install grpcio
RUN ./script/install-grpc
RUN ./script/generate
