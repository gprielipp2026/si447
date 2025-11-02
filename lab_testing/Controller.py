from threading import Thread
from CustomExceptions import *
from State import State
from ServerModel import ServerModel
from UserModel import UserModel
from View import View

class Controller:
  def __init__(self, view, user, server):
    self.view: View = view
    self.user: UserModel = user
    self.server: ServerModel = server
    self.state = State.start

  def run(self):
    # capture all input
    running = True
    while running:
      if self.state == State.start:
        self.view.showStart()
        option = self.view.getInput()
        if option == '1':
          self.state = State.signup
          self.view.signup()
        elif option == '2':
          self.state = State.login
          self.view.login()
      elif self.state == State.stop:
        running = False
      elif self.state == State.signup:
        username, password = self.view.getInput(), self.view.getInput()
        self.user.setUsername(username)
        self.user.setPassword(password)

        try:
          msg = self.user.signup(self.server)
          self.view.success(msg)
          self.state = State.exploring
        except UserExists as e:
          self.view.error(f'User already exists: {str(e)}')
        except ValidationError as e:
          self.view.error(f'Server validation error: {str(e)}')
        except UnexpectedServerResponseCode as e:
          self.view.error(f'Unexpected server response code: {str(e)}')
        finally:
          self.view.proceed()

      elif self.state == State.login:
        username, password = self.view.getInput(), self.view.getInput()
        self.user.setUsername(username)
        self.user.setPassword(password)

        try:
          self.user.login(self.server)
          self.state = State.exploring
        except InvalidLoginAttempt as e:
          self.view.error(f'Invalid login attempt: {str(e)}')
        except ValidationError as e:
          self.view.error(f'Server validation error: {str(e)}')
        except UnexpectedServerResponseCode as e:
          self.view.error(f'Unexpected server response code: {str(e)}')
        finally:
          self.view.proceed()

      elif self.state == State.exploring:
        inpmap = {
          'move': self.server.move,
          'look': self.server.look,
          'do': self.server.doSomething,
          'use': self.server.useItem,
        }
        
        cmd = self.view.getInput().lower()

        try:
          if cmd == 'stop' or cmd == 'quit':
            self.state = State.stop
          elif cmd in ['move','do', 'use']:
            extra = self.view.getInput()
            res = inpmap[cmd](self.user.getToken(), extra)
            self.view.display(res)
          else:
            res = inpmap[cmd](self.user.getToken())
            self.view.display(res)
        except InvalidDirectionOrMovement as e:
          self.view.error(f'Invalid movement or direction: {str(e)}')
        except ItemNotFound as e:
          self.view.error(f'Item was not found: {str(e)}')
        except ValidationError as e:
          self.view.error(f'Server validation error: {str(e)}')
        except UnexpectedServerResponseCode as e:
          self.view.error(f'Unexpected server response code: {str(e)}')
        finally:
          self.view.proceed()

    
