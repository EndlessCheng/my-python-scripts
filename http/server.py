from datetime import datetime
import socket


def handle(rfile, wfile):
    try:
        recv = rfile.readline(1024)
        print(len(recv), recv.decode())

        if not recv:
            return
        while True:
            line = rfile.readline(1024)
            if line in (b'\r\n', b'\n', b''):
                break

        # TODO: 显然代码还有很多地方有重构的味道，这正是框架慢慢形成的起因
        wfile.sendall(f"{datetime.now().replace(microsecond=0)}".encode())
    except socket.timeout as e:
        print(f"Request timed out: {e}")


print('http://127.0.0.1:8000')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind(('127.0.0.1', 8000))
    server_socket.listen(5)
except:
    server_socket.close()
    raise

print('looping...')

while True:
    try:
        # socketserver 首要做的就是在 socket 层面创建 client_socket
        client_socket, _ = server_socket.accept()
    except OSError as e:
        print(f"server_socket.accept() error: {e}")
        continue
    try:
        # 如何管理网络 I/O，这是 handler 做的（socket 层面）
        rfile = client_socket.makefile('rb')  # buffered，方便处理
        wfile = client_socket

        # http 层面上的 handler，这是上层所关心的
        handle(rfile, wfile)

        client_socket.close()
        rfile.close()
    except Exception as e:
        print(f"handle error {e}")
