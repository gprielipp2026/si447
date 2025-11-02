from CustomExceptions import *
from ServerModel import ServerModel
from UserModel import UserModel
from View import View
from Controller import Controller

class App:
  def __init__(self):
    self.view = View()
    self.user = UserModel()
    self.server = ServerModel('http://lnx1073302govt:8000')

    self.controller = Controller(self.view, self.user, self.server)

  def start(self):
    # start the app
    self.controller.run()

    # wait for the app to close
    # self.controller.join()

if __name__ == '__main__':
  app = App()

  app.start()
