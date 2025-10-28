import requests

class ServerModel:
  def __init__(self, url) -> None:
    self.url = url

  def create(self, username, password) -> dict:
    resp = requests.post(
      self.url + '/user',
      {
        'username': username,
        'password': password
      }
    )

    return {}

  def login(self, username, password) -> dict:
    return {}

  def move(self, direction) -> dict:
    return {}

  def look(self) -> dict:
    return {}

  def doSomething(self, action) -> dict:
    return {}

  def useItem(self, item) -> dict:
    return {}

  def getPlayers(self) -> dict:
    return {}