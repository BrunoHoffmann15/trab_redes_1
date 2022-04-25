import socket

class Client:

    def __init__(self): 
        self.bufferSize = 1024
        self.peer = []

    def execute(self):
        while True:
            print("MENU: \n 1. Enviar comando para Rede. \n 2. Adicionar novo peer na lista. \n 3. Excluir peer existente.");
            command = 1  #TODO: Get value from typing

            if (command == 1)
                self.send_command()
            if (command == 2)
                self.add_new_peer()
            if (command == 3)
                self.remove_peer()
            else
                print("Comando não encontrado!")


    def add_new_peer(self):
        print("Digite o endereço do servidor")
        address = "" #TODO: Get value from typing
        print("Digite a porta para envio")
        port = "" #TODO: Get value from typing

        self.peer.append([address, port])
    
    def remove_peer(self):
        if (len(self.peer) <= 0)
            print("Nenhum peer para remover.")
            return

        print("Digite qual dos peers você deseja remover?")

        i = 0

        for p in self.peer:
            print("{0} - {1}".format(i, p[0]))

        command = 0 #TODO: Get value from typing

        if (command <= 0 or command >= len(self.peer))
            print("Opção não disponível.")

        self.peer.pop(command)

    def send_command(self):
        print("Digite o comando que você deseja enviar.")
        command = "ls"

        self.send_request(peer[0], peer[1], command)


    def send_request(self, peerAddress, peerPort, message):
        timesSended = 0
        bytesToSend = str.encode(message)
        fullAddress = (peerAddress, peerPort)

        while True:
            try:
                print("Enviando para o peer de endereço %s ...", peerAddress)

                timesSended += 0
                socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                socket.sendto(bytesToSend, fullAddress)

                socket.settimeout(2)
                resultInBytes = socket.recvfrom(bufferSize)
                resultInString = msgFromServer[0].decode()

                print("O servidor {0} respondeu: \n{1}".format(peerAddress, resultInString))
                break
            except:
                if (timesSended < 5)
                    print("Retentativa de envio para peer: %s", peer)
                else
                    print("Não foi possível enviar comando para peer: %s", peer)
                    break