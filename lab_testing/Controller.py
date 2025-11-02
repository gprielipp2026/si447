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
        elif option == 'stop' or option == 'quit':
          self.state = State.stop

      elif self.state == State.stop:
        running = False

      elif self.state == State.signup:
        username, password = self.view.getInput(), self.view.getInput()
        self.user.setUsername(username)
        self.user.setPassword(password)

        try:
          msg = self.user.signup(self.server)
          self.view.success(msg)
          msg = self.user.login(self.server)
          self.state = State.exploring
          self.view.proceed()
        except UserExists as e:
          self.view.error(f'User already exists: {str(e)}')
          self.state = State.start
        except ValidationError as e:
          self.view.error(f'Server validation error: {str(e)}')
          self.state = State.start
        except UnexpectedServerResponseCode as e:
          self.view.error(f'Unexpected server response code: {str(e)}')
          self.state = State.start

      elif self.state == State.login:
        username, password = self.view.getInput(), self.view.getInput()
        self.user.setUsername(username)
        self.user.setPassword(password)

        try:
          self.user.login(self.server)
          self.state = State.exploring
          self.view.proceed()
        except InvalidLoginAttempt as e:
          self.view.error(f'Invalid login attempt: {str(e)}')
          self.state = State.start
        except ValidationError as e:
          self.view.error(f'Server validation error: {str(e)}')
          self.state = State.start
        except UnexpectedServerResponseCode as e:
          self.view.error(f'Unexpected server response code: {str(e)}')
          self.state = State.start

      elif self.state == State.exploring:
        inpmap = {
          'move': self.server.move,
          'look': self.server.look,
          'do': self.server.doSomething,
          'use': self.server.useItem,
        }
        
        viewmap = {
          'move': self.view.move,
          'do': self.view.do,
          'use': self.view.use
        }

        cmd = self.view.getInput().lower()

        try:
          if cmd == 'stop' or cmd == 'quit':
            self.state = State.stop
          elif cmd in ['move','do', 'use']:
            viewmap[cmd]()
            extra = self.view.getInput()
            res = inpmap[cmd](self.user.getToken(), extra)
            self.view.display(res)
          elif cmd in ['look']:
            res = inpmap[cmd](self.user.getToken())
            self.view.display(res)
          else:
            self.view.error(f'Unknown command: {cmd}')
        except InvalidDirectionOrMovement as e:
          self.view.error(f'Invalid movement or direction: {str(e)}')
        except ItemNotFound as e:
          self.view.error(f'Item was not found: {str(e)}')
        except ValidationError as e:
          self.view.error(f'Server validation error: {str(e)}')
        except UnexpectedServerResponseCode as e:
          self.view.error(f'Unexpected server response code: {str(e)}')
        finally:
          if not cmd in ['stop', 'quit']:
            self.view.proceed()

    
