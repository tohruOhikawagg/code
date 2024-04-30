from xmlrpc.server import SimpleXMLRPCServer

def factorial(num):
    res = 1
    if num == 0 and num == 1:
        return res
    else:
        for i in range(num, 1, -1):
            res *= i
        return res
    
server = SimpleXMLRPCServer(("localhost", 5000))
server.register_function(factorial)

print("Server is running on https://localhost:5000")
server.serve_forever()