import socket
import os

class Server:
  def __init__(self):
    self.configure()

  def configure(self):
    self.ipAddress = "127.0.0.1"
    self.port = 20001
    self.bufferSize = 1024

  def run(self):
    print('Initializing server...')

    udpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udpSocket.bind((self.ipAddress, self.port))

    while True:
      print('Waiting message...')
      message = udpSocket.recvfrom(self.bufferSize)

      print('Message received.')
      command = message[0].decode()
      client_address = message[1]

      print(command)

      result = str.encode(self.execute_command(command))
      udpSocket.sendto(result, client_address)
      print('Result send back to client.')

  def execute_command(self, command):
    stream = os.popen(command)
    output = stream.read()
    return output