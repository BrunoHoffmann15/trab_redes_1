import socket
import os

class Server:
  def __init__(self):
    self.configure()

  def configure(self):
    hostname = socket.gethostname()
    self.ipAddress = socket.gethostbyname(hostname)
    self.port = 20001
    self.bufferSize = 1024

  def run(self):
    print('Inicializando servidor...')

    udpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udpSocket.bind((self.ipAddress, self.port))

    while True:
      print('Esperando mensagem...')
      message = udpSocket.recvfrom(self.bufferSize)

      print('Mensagem recebida.')
      command = message[0].decode()
      client_address = message[1]

      print(command)

      result = str.encode(self.execute_command(command))
      udpSocket.sendto(result, client_address)
      print('Enviando mensagem de volta para cliente.')

  def execute_command(self, command):
    stream = os.popen(command)
    output = stream.read()
    return output