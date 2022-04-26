import socket
import threading
import time

class Client:

    def __init__(self): 
        self.bufferSize = 1024
        self.peer = []

    def execute(self):
        while True:
            try:
                print("[Client] MENU: \n 1. Enviar comando para Rede. \n 2. Adicionar novo peer na lista. \n 3. Excluir peer existente. \n 4. Finalizar");
                command = int(input("[Client] Digite o ação que você deseja.\n"))
                
                if (command == 1):
                    self.send_command()
                elif (command == 2):
                    self.add_new_peer()
                elif (command == 3):
                    self.remove_peer()
                else:
                    print("[Client] Finalizando aplicação.")
                    return
            except Exception as e:
                print("[Client]", e)
                print("[Client] Ocorreu um erro durante o processo.")


    def add_new_peer(self):
        address = input("[Client] Digite o endereço do servidor\n")
        port = int(input("[Client] Digite a porta para envio\n"))
        
        self.peer.append([address, port])
    
    def remove_peer(self):
        if (len(self.peer) <= 0):
            print("[Client] Nenhum peer para remover.")
            return

        print("[Client] Peers:")

        i = 0

        for p in self.peer:
            print("[Client] {0} - {1}".format(i, p[0]))
            i += 1

        command = int(input("[Client] Digite qual dos peers você deseja remover?\n"))

        if (command < 0 or command >= len(self.peer)):
            print("[Client] Opção não disponível.")
            return

        self.peer.pop(command)

    def send_command(self):
        if (len(self.peer) <= 0):
            print("[Client] Adicione um peer antes.")
            return

        command = input("[Client] Digite o comando que você deseja enviar.\n")

        for p in self.peer:
            self.send_request(p[0], p[1], command)


    def send_request(self, peerAddress, peerPort, message):
        timesSended = 0
        bytesToSend = str.encode(message)
        fullAddress = (peerAddress, peerPort)

        while True:
            try:
                print("[Client] Enviando para o peer de endereço %s ...", peerAddress)

                udpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                udpSocket.sendto(bytesToSend, fullAddress)

                udpSocket.settimeout(2)
                resultInBytes = udpSocket.recvfrom(1024)
                resultInString = resultInBytes[0].decode()

                print("[Client] O peer {0} respondeu: \n{1}".format(peerAddress, resultInString))
                break
            except Exception as e:
                print("[Client]", e)

                if (timesSended < 5):
                    print("[Client] Retentativa de envio para peer: %s", peer)
                else:
                    print("[Client] Não foi possível enviar comando para peer: %s", peer)
                    break