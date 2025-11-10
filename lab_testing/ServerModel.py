import requests
from CustomExceptions import *
import json

class ServerModel:
    def __init__(self, url) -> None:
        self.url = url

    def create(self, username, password) -> str:
        resp = requests.post(
            self.url + '/user',
            data=json.dumps({
                'username': username,
                'password': password
            })
        )

        if resp.status_code == 200:
            return resp.json()['message']
        elif resp.status_code == 400:
            raise UserExists('Username already exists')
        elif resp.status_code == 422:
            # validation error
            resp = resp.json()['detail'][0]
            raise ValidationError(f'{resp["type"]}: {resp["msg"]}')
        else:
            raise UnexpectedServerResponseCode(f'Unexpected response code: {resp.status_code}')

    def login(self, username, password) -> str:
        resp = requests.post(
            self.url + '/login',
            data=json.dumps({
                'username': username,
                'password': password
            })
        )

        if resp.status_code == 200:
            return resp.json()['session_token']
        elif resp.status_code == 400:
            raise InvalidLoginAttempt('Username or Password are incorrect')
        elif resp.status_code == 422:
            # validation error
            resp = resp.json()['detail'][0]
            raise ValidationError(f'{resp["type"]}: {resp["msg"]}')
        else:
            raise UnexpectedServerResponseCode(f'Unexpected response code: {resp.status_code}')

    def move(self, token, direction) -> str:
        resp = requests.post(
            self.url + '/move',
            data=json.dumps({
                'direction': direction
            }),
            headers={
                'session-token': token
            }
        ) 

        if resp.status_code == 200:
            return resp.json()['message']
        elif resp.status_code == 400:
            raise InvalidDirectionOrMovement('Username or Password are incorrect')
        elif resp.status_code == 422:
            # validation error
            resp = resp.json()['detail'][0]
            raise ValidationError(f'{resp["type"]}: {resp["msg"]}')
        else:
            raise UnexpectedServerResponseCode(f'Unexpected response code: {resp.status_code}')

    def look(self, token) -> str:
        resp = requests.get(
            self.url + '/look',
            headers={
                'session-token': token
            }
        )

        if resp.status_code == 200:
            return resp.json()['description']
        elif resp.status_code == 422:
            # validation error
            resp = resp.json()['detail'][0]
            raise ValidationError(f'{resp["type"]}: {resp["msg"]}')
        else:
            raise UnexpectedServerResponseCode(f'Unexpected response code: {resp.status_code}')

    def doSomething(self, token, action) -> str:
        resp = requests.post(
            self.url + '/doing',
            data=json.dumps({
                'action': action
            }),
            headers={
                'session-token': token
            }
        )
        
        if resp.status_code == 200:
            return resp.json()['message']
        elif resp.status_code == 422:
            # validation error
            resp = resp.json()['detail'][0]
            raise ValidationError(f'{resp["type"]}: {resp["msg"]}')
        else:
            raise UnexpectedServerResponseCode(f'Unexpected response code: {resp.status_code}')

    def useItem(self, token, item) -> dict:
        resp = requests.post(
            self.url + '/use',
            data=json.dumps({
                'item': item
            }),
            headers={
                'session-token': token
            }
        )
        
        if resp.status_code == 200:
            return resp.json()['message']
        elif resp.status_code == 400:
            raise ItemNotFound('Username or Password are incorrect')
        elif resp.status_code == 422:
            # validation error
            resp = resp.json()['detail'][0]
            raise ValidationError(f'{resp["type"]}: {resp["msg"]}')
        else:
            raise UnexpectedServerResponseCode(f'Unexpected response code: {resp.status_code}')

    def getPlayers(self) -> dict:
        resp = requests.get(
            self.url + '/players'
        )
        
        if resp.status_code == 200:
            return resp.json()['players']
        else:
            raise UnexpectedServerResponseCode(f'Unexpected response code: {resp.status_code}')
