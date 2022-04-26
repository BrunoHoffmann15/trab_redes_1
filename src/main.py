from thread_control import ThreadControl
import sys

import time

if __name__ == "__main__":
  threadControlServer = ThreadControl(1)
  threadControlClient = ThreadControl(2)

  threadControlServer.start()
  time.sleep(2)
  threadControlClient.start()