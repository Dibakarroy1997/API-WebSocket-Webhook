from xmlrpc.client import ServerProxy

proxy = ServerProxy("http://localhost:8082", verbose=True)

if __name__ == "__main__":
    print(proxy.add(1, 2))
    print(proxy.sub(3, 1))
