from  ServerModel import *

class TestServerModel:
  def beforeEach(self):
    self.server = ServerModel('http://lnx1073302govt:8000')

  def test_create(self):
    self.beforeEach()

    res = self.server.create("user", "pass")

    assert ('message' in res)

