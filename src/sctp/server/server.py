import socket
import sctp
import os

class Server:
  def __init__(self):
    self.configure()

  def configure(self):
    hostname = socket.gethostname()
    self.ipAddress = socket.gethostbyname(hostname)
    #self.ipAddress = self.execute_command('hostname -I').strip() # descomente em caso de executar em VM Linux
    self.port = 22223
    self.bufferSize = 1024
    print("[Server] Ip address:", self.ipAddress)
    print("[Server] Port:", self.port)

  def execute(self):
    print('[Server] Inicializando servidor...')

    sctpSocket = sctp.sctpsocket_tcp(socket.AF_INET)
    
    sctpSocket.bind((self.ipAddress, self.port))
    sctpSocket.listen(5)

    while True:
      print('[Server] Esperando conexão...')
      connection, clientAddress = sctpSocket.accept()
      print('[Server] Conexão feita com ', clientAddress)

      print('[Server] Esperando mensagem...')
      data = connection.sctp_recv(self.bufferSize)
      message = data[2]

      print('[Server] Mensagem recebida.')
      command = message.decode()

      print("[Server] Comando: ", command)
      
      result = str.encode(self.execute_command(command))
      connection.sctp_send(result)

      print('[Server] Enviando mensagem de volta para cliente.')
      connection.close()

    sctpSocket.close()

  def execute_command(self, command):
    stream = os.popen(command)
    output = stream.read()
    return output