# GRPC with Python

This is an example [GRPC](http://grpc.io) application using Python. The IDL in `protos/kv.proto` defines a simple Key/Value store.

## Getting started

[Install GRPC for Python](https://github.com/grpc/grpc/tree/master/src/python/grpcio)

Depending on your system, you may not need to do most of these steps.  However, if you are starting from scratch with Python, follow the instructions for you OS.

### Update Python to 2.7

**OSX**

```bash
brew install python # or brew upgrade python
```

**Windows Installers**

[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

**Linux**

```bash
apt-get install python
```

### Install Protobuf

**Mac/Linux**

```bash
curl -fsSL https://goo.gl/getgrpc | bash -s plugins
```

**Windows**

Download the Installer

[https://github.com/google/protobuf/releases/download/v3.0.0-beta-2/protoc-3.0.0-beta-2-win32.zip](https://github.com/google/protobuf/releases/download/v3.0.0-beta-2/protoc-3.0.0-beta-2-win32.zip)

### Install gRPC

```bash
pip install grpcio
```

## Generate the Python GRPC stubs.

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


