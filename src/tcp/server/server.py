import socket
import os

class Server:
  def __init__(self):
    self.configure()

  def configure(self):
    hostname = socket.gethostname()
    self.ipAddress = socket.gethostbyname(hostname)
    #self.ipAddress = self.execute_command('hostname -I').strip() # descomente em caso de executar em VM Linux
    self.port = 1024
    self.bufferSize = 1024
    print("[Server] Ip address:", self.ipAddress)
    print("[Server] Port:", self.port)

  def execute(self):
    print('[Server] Inicializando servidor...')

    tcpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    
    tcpSocket.bind((self.ipAddress, self.port))
    tcpSocket.listen(5)

    while True:
      print('[Server] Esperando conexão...')
      connection, clientAddress = tcpSocket.accept()
      print('[Server] Conexão feita com ', clientAddress)

      print('[Server] Esperando mensagem...')
      message = connection.recv(self.bufferSize)

      print('[Server] Mensagem recebida.')
      command = message.decode()

      print("[Server] Comando: ", command)
      
      result = str.encode(self.execute_command(command))
      connection.send(result)

      print('[Server] Enviando mensagem de volta para cliente.')
      connection.close()

    tcpSocket.close()

  def execute_command(self, command):
    stream = os.popen(command)
    output = stream.read()
    return output