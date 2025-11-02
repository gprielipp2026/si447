class InvalidLoginAttempt(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(args, kwargs)

class ValidationError(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(args, kwargs)

class InvalidDirectionOrMovement(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(args, kwargs)

class ItemNotFound(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(args, kwargs)

class UserExists(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(args, kwargs)

class UnexpectedServerResponseCode(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(args, kwargs)

class UserLoginError(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(args, kwargs)

class UserNotLoggedIn(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(args, kwargs)