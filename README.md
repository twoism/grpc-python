# GRPC with Python

This is an example [GRPC](http://grpc.io) application using Python. The IDL in `protos/kv.proto` defines a simple Key/Value store.

## Getting started

[Install GRPC for Python](https://github.com/grpc/grpc/tree/master/src/python/grpcio)

Update Python

```bash
brew install python
```

Install gRPC

```bash
pip install grpcio
```

Then generate the Python GRPC stubs.

```bash
./script/generate
```

## Start the server

```bash
./script/server
```

## Using the client
```bash
./script/client

script/client usage:
  script/client set <key> <value> - sets the <key> and <value>
  script/client get <key>         - gets the value for <key>
```


