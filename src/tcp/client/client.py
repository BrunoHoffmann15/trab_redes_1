import socket

class Client:

    def __init__(self): 
        self.bufferSize = 1024
        self.peers = []

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
                print("[Client] Erro: ", e)

    def add_new_peer(self):
        address = input("[Client] Digite o endereço do servidor\n")
        port = int(input("[Client] Digite a porta para envio\n"))
        
        self.peers.append([address, port])
    
    def remove_peer(self):
        if (len(self.peers) <= 0):
            print("[Client] Nenhum peer para remover.")
            return

        print("[Client] Peers:")

        i = 0

        for p in self.peers:
            print("[Client] {0} - {1}".format(i, p[0]))
            i += 1

        command = int(input("[Client] Digite qual dos peers você deseja remover?\n"))

        if (command < 0 or command >= len(self.peers)):
            print("[Client] Opção não disponível.")
            return

        self.peers.pop(command)

    def send_command(self):
        if (len(self.peers) <= 0):
            print("[Client] Adicione um peer antes.")
            return

        command = input("[Client] Digite o comando que você deseja enviar.\n")

        for p in self.peers:
            self.send_request(p[0], p[1], command)


    def send_request(self, peerAddress, peerPort, message):
        timesSended = 0
        bytesToSend = str.encode(message)
        fullAddress = (peerAddress, peerPort)

        while True:
            try:
                print("[Client] Enviando para o peer de endereço %s ..." % (peerAddress))

                timesSended += 1

                tcpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
                
                tcpSocket.connect(fullAddress)

                tcpSocket.send(bytesToSend)

                print("[Client] Comando enviado para o peer de endereço %s ..." % (peerAddress))

                resultInBytes = tcpSocket.recv(self.bufferSize)
                resultInString = resultInBytes.decode()

                print("[Client] O peer {0} respondeu: \n{1}".format(peerAddress, resultInString))
                break
            except Exception as e:
                print("[Client] Erro: ", e)

                if (timesSended < 5):
                    print("[Client] Retentativa de envio para peer: %s", peerAddress)
                else:
                    print("[Client] Não foi possível enviar comando para peer: %s", peerAddress)
                    break

                