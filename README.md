# Trabalho de Redes GA
Aluno: Bruno da Siqueira Hoffmann

Professor: Cristiano Bonato Both

Instituição: Universidade do Vale dos Sinos - São Leopoldo

## Requisitos do Trabalho

- Organização da apresentação oral de como o projeto foi concebido.

- Criação do servidor.

- Criação do cliente.

- Integração do cliente e servidor em um sistema

- Envio de comandos para os peers

- Execução dos comandos em cada peer da rede

- Coleta e envio da resposta do comando para o peer que disparou o comando

- Apresentação das informações para cada peer envolvido

- Testar o software em no mínimo dois ambientes diferentes, i.e., Máquinas Virtual, Bare
metal, Containers, plataforma em nuvem, etc.

- Adição de um novo nodo (peer) na rede.

## Requisitos para Executar
- Necessidade de ter a versão 3 do python. Disponível [aqui](https://www.python.org/downloads/).

## Estrutura de Pastas
- `src`: Solução da aplicação.
  - `main.py`: faz a inicialização das threads.

  - `thread_control.py`: faz a criação do client ou do server, e mantém esses na thread.

  - `/server/server.py`: realiza o recebimento de dados de algum client, faz a execução dos comandos no sistema do peer e retorna para o client.

  - `/client/client.py`: realiza o envio de dados para o server, além de fazer o controle lógico da rede.

- `tests`: Demonstração dos testes executados:
  - `Ambiente Containerizado`: Apresentação de alguns cenários de testes executados no ambiente Docker container.

  - `Ambiente Maquina Virtual`: Apresentação de alguns cenários de testes executados no ambiente Maquina Virtual.

- `docs`: Documentos relacionados aos requisitos do trabalho e a apresentação.

## Como Executar
- Esse projeto é compatível com os sistemas operacionais Windows, Linux e MacOS. Para execução dele, foi testado através do uso de um ambiente de containers docker e também através de várias máquinas virtuais Linux.

### Configurando Máquina Virtual
- Configurar uma máquina virtual linux;

- Configurar uma Rede NAT;

- Configurar essa rede para as máquinas virtuais e gerar novo endereço MAC;

- Executar a máquina virtual;

- Fazer a instalação do python e git através do apt-get:
  ```cmd
  $ sudo apt-get install python3.6 
  $ sudo apt-get install git-all
  ```
- Fazer o clone do repositório git:
  ```cmd
  $ git clone https://github.com/BrunoHoffmann15/trab_redes_1_ga.git
  ```
- Abrir o terminal na pasta baixada;
- Acessar a pasta **/src/**
  ```cmd
  $ cd src/
  ```
- Executar a aplicação:
  ```cmd
  $ python3 main.py
  ```
- Vídeo de Demo: [Clique aqui](https://www.youtube.com/watch?v=Numb4kRI2D4);

### Configurando Docker
- Rodar comando `docker build --tag python-udp .` para gerar uma imagem docker;

- Executar o comando docker run pela quantidade de peers;
  ```cmd
  $ docker run -d --name peer1 -p 6000 -t python-udp
  $ docker run -d --name peer2 -p 6001 -t python-udp
  $ docker run -d --name peer3 -p 6002 -t python-udp
  ```

- Entrar nos containers:
  ```cmd
  $ docker exec -it <ID_CONTAINER> /bin/sh
  ```

- Executar inicialização da aplicação:
  ```cmd
  python main.py
  ```
  
- Vídeo de Demo: [Clique aqui](https://www.youtube.com/watch?v=KovU0GtMWJE);

## Referências usadas
- [UDP - Client And Server Example Programs In Python](https://pythontic.com/modules/socket/udp-client-server-example)
- [Socket Básico](https://wiki.python.org.br/SocketBasico)
- [Thread](https://www.tutorialspoint.com/python/python_multithreading.htm)
- [Dockerfile](https://docs.docker.com/language/python/build-images/)
- [How to Execute Shell Commands with Python](https://janakiev.com/blog/python-shell-commands/)