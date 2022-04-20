import socket

class Server:
  def configure(self):
    self.ipAddress = "127.0.0.1"
    self.port = 20001
    self.bufferSize = 1024

  def initialize():
    self.configure()

    udpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udpSocket.bind(self.ipAddress, self.port)

    while True:
      command = udpSocket.recvfrom(bufferSize)
      result = self.execute_command(command)

      # TODO: Send back the command result to client.

  def execute_command(command):
    # TODO: Execute the command and return result.
    return 'resultado'

