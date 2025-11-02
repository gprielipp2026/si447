from typing import Any
from ServerModel import ServerModel
from CustomExceptions import *

class UserModel:
  def __init__(self):
    self.token = None
    self.username = None
    self.password = None

  def __checkToken(self):
    if self.token is None:
      raise UserNotLoggedIn('User is not logged in')

  def __checkCreds(self):
    if self.username is None or self.password is None:
      raise UserLoginError("Need to have a username and password")

  def setUsername(self, username):
    self.username = username

  def setPassword(self, password):
    self.password = password

  def signup(self, server: ServerModel):
    self.__checkCreds()

    return server.create(self.username, self.password)

  def login(self, server: ServerModel):
    self.__checkCreds()

    self.token = server.login(self. username, self.password)

  def getToken(self):
    self.__checkToken()

    return self.token