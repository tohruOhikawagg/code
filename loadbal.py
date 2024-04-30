from itertools import cycle

class LoadBalancer:
    def __init__(self, servers):
        self.servers = cycle(servers)
    def get_server(self):
        return next(self.servers)
    
if __name__ == '__main__':
    servers = ['server 1', 'server 2', 'server 3', 'server 4', 'server 5']
    lb = LoadBalancer(servers=servers)

    for job in range(17):
        server = lb.get_server()
        print(f'Request for job {job} is handled by {server}')