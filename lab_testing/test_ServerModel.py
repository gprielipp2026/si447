from  ServerModel import *
from CustomExceptions import *
import pytest

class TestServerModel:
  def beforeEach(self):
    self.server = ServerModel('http://lnx1073302govt:8000')

  def test_create(self):
    self.beforeEach()

    with pytest.raises(UserExists):
      res = self.server.create("user", "pass") # already created

  def test_login(self):
    self.beforeEach()

    res = self.server.login("user", "pass")

  def test_look(self):
    self.beforeEach()

    tok = self.server.login("user", "pass")
    
    res = self.server.look(tok)

    

