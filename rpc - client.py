from xmlrpc.client import ServerProxy

server_proxy = ServerProxy("http://localhost:5000")

output = server_proxy.factorial(5)

print(f'Factorial of the given number is {output}')