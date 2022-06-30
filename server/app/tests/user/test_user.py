import pytest
import random
import string
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

token = None
email = random_string(5) + '@gmail.com'
username = random_string(5)
password = random_string(5)

def test_sign_up():
    global token
    response = client.post("auth/sign-up", json={'email': email, 'username': username, 'password': password})
    assert response.status_code == 200
    response = client.post("auth/sign-in", data={'username': username, 'password': password})
    assert response.status_code == 200
    token = response.json()['access_token']
def test_token():
    response = client.get("auth/user", headers={'Authorization': 'Bearer ' + token})
    assert response.status_code == 200
    assert response.json()['email'] == email and response.json()['username'] == username
