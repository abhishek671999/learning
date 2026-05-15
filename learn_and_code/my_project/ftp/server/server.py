from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler

address = ("127.0.0.1", 21)  # listen on every IP on my machine on port 21
server = servers.FTPServer(address, FTPHandler)
server.serve_forever()