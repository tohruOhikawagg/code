import socket

def get_ip_address(url):
    try:
        host_name = socket.gethostbyname(url)
        host_ip = socket.gethostbyname(host_name)
        print("Hostname:", host_name)
        print("IP:", host_ip)
    except:
        print("Unable to get hostname and IP")

if __name__ == '__main__':
    url = "www.google.com"
    get_ip_address(url)
