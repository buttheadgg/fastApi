import pytest
import random
import string

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def test_sign_up():
    data = [
        {
            'request': {'email': random_string(5) + '@gmail.com', 'username': random_string(5), 'password': random_string(5)},
            'response': 200
        },
    ]
    for d in data:
        # reg new user
        response = client.post("auth/sign-up", json=d['request'])
        assert response.status_code == d['response']
        

def test_sign_in():
    data = [
        {
            'request': {'email': random_string(5) + '@gmail.com', 'username': random_string(5), 'password': random_string(5)},
            'response': 200
        },
    ]
    for d in data:
        # reg new user
        response = client.post("auth/sign-up", json=d['request'])
        assert response.status_code == d['response']
        # login
        response = client.post("auth/sign-in", data=d['request'])
        assert response.status_code == d['response']
        assert isinstance(response.json()['access_token'], str)

def test_get_user():
    data = [
            {
                'request': {'email': random_string(5) + '@gmail.com', 'username': random_string(5), 'password': random_string(5)},
                'response': 200
            },
        ]
    for d in data:
        # reg new user
        response = client.post("auth/sign-up", json=d['request'])
        assert response.status_code == d['response']
        assert isinstance(response.json()['access_token'], str)
        # get token
        token = response.json()['access_token']
        # get user info
        response = client.get("auth/user", headers={'Authorization': 'Bearer ' + token})
        assert response.status_code == d['response']
        assert response.json()['email'] == d['request']['email'] and response.json()['username'] == d['request']['username']
