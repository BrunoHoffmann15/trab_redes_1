import threading
import time

from server.server import Server
from client.client import Client


class ThreadControl(threading.Thread):
    def __init__(self, type):
        threading.Thread.__init__(self)
        self.type = type

    def run(self):
        if (self.type == 1):
            server = Server()
            server.execute()
        else:
            client = Client()
            client.execute()