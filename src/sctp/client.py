import socket
import sctp

hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)

sk = sctp.sctpsocket_tcp(socket.AF_INET)
sk.connect((ipAddress, 36412))

sk.sctp_send(msg='hello world')
sk.close()