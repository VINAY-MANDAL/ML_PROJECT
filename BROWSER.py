import socket

class URL:
    def request(self):
        s = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=socket.IPPROTO_TCP,
        )

class URL:
    def request(self):
        s.connect((self.host, 80))