from threading import Thread
from CustomExceptions import *
import getpass 

class View:
  def __init__(self):
    self.inputs = []

  def getInput(self) -> str:
    return self.inputs.pop()
  
  def display(self, msg):
    print()
    print(msg)
    print()

  def input(self, prompt='> '):
    res = input(prompt)
    self.inputs.append(res)

  def showStart(self):
    self.display("~~ Welcome to MidsQuest! ~~")
    self.display("1. Sign up\n2. Log in")

    self.input()

  def __credentials(self):
    print()
    self.input('Username: ')
    pswd = getpass.getpass(prompt='Password: ', mask='*')
    print()
    self.inputs.append(pswd)

  def signup(self):
    self.__credentials()

  def login(self):
    self.__credentials()

  def proceed(self):
    self.input()

  def success(self, msg):
    self.display('Success!')
    self.display(msg)

  def error(self, msg):
    self.display('Error!')
    self.display(msg)
