from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("localhost", 8082), logRequests=True)


class Calculator:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y


server.register_instance(Calculator())


if __name__ == "__main__":
    try:
        print("Starting server...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopping server...")
