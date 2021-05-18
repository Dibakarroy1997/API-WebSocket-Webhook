### Generate request and response classes along with client and server classes
```bash
poetry run python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --proto_path=. grpc_example/proto/calculator.proto
```

### How to start evans
```bash
grpc_example/evans/evans.exe --path grpc_example/proto calculator.proto -r
```