import requests

class Commander:
    """
    Interface to the Mids Quest API.
    This class is responsible for translating commands in our system to API calls.
    """

    def __init__(self):
        self.logged_in = False    

    def create_user(self, username, password):
        """
        This function asks the API to create a new user. If the response
        is 200, the user was created successfully. If 400, the user was 
        not created successfully
        """
        
        url = "http://lnx"

        body = {
            "username": username,
            "password": password
        }

    def login(self, username, password):
        """
        If successful, set self.logged_in to be true.
        If not, throw an Exception
        """
        url = "http://lnx1073302govt:8000/user"

        body = {
            "username": username,
            "password": password
        }

        response = requests.post(
            url,
            json=body
        )

        if response.status_code == 200:
            parsed_response = response.json()
            self.session_token = parsed_response["session_token"]
            self.logged_in = True

        raise Exception


    def logged_in(self):
        return self.logged_in

