import socket
import sctp

hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)

sock = sctp.sctpsocket_tcp(socket.AF_INET)
sock.bind((ipAddress, 36412))
sock.listen(1)

while True: 
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection recebida')
        data = connection.sctp_recv(1024)

        message = data[2]
        print("Message: ", message)

    finally:
        # Clean up the connection
        connection.close()