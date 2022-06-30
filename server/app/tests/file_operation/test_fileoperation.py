from fastapi.testclient import TestClient
from app.main import app
from app.tests.user.test_user import random_string
import uuid

client = TestClient(app)

def test_upload_file():
    data = [
        {
            'request': {'email': random_string(5) + '@gmail.com', 'username': random_string(5), 'password': random_string(5)},
            'response': 200
        },
    ]
    files = [
        {
            'request': {"files": ("test.png", open('./app/tests/file_operation/test.png', "rb"), "image/jpeg")},
            'response': 200
        },
    ]
    for i in range(0, len(files)):
      # reg new user
      response = client.post("auth/sign-up", json=data[i]['request'])
      assert response.status_code == data[i]['response']
      assert isinstance(response.json()['access_token'], str)
      # get token
      token = response.json()['access_token']
      response = client.post("FileOperations/frames", headers={'Authorization': 'Bearer ' + token}, files=files[i]['request'])
      assert response.status_code == files[i]['response']

def test_get_data():
    data = [
        {
            'request': {'email': random_string(5) + '@gmail.com', 'username': random_string(5), 'password': random_string(5)},
            'response': 200
        },
    ]
    files = [
        {
            'request': {"files": ("test.png", open('./app/tests/file_operation/test.png', "rb"), "image/jpeg")},
            'response': 200
        },
    ]
    for i in range(0, len(files)):
      # reg new user
      response = client.post("auth/sign-up", json=data[i]['request'])
      assert response.status_code == data[i]['response']
      assert isinstance(response.json()['access_token'], str)
      # get token
      token = response.json()['access_token']
      response = client.post("FileOperations/frames", headers={'Authorization': 'Bearer ' + token}, files=files[i]['request'])
      assert response.status_code == files[i]['response']
      # get code
      code = response.json()['result']
      response = client.get(f"FileOperations/frames/{code}", headers={'Authorization': 'Bearer ' + token})
      assert response.status_code == files[i]['response']

def test_delete_data():
    data = [
        {
            'request': {'email': random_string(5) + '@gmail.com', 'username': random_string(5), 'password': random_string(5)},
            'response': 200
        },
    ]
    files = [
        {
            'request': {"files": ("test.png", open('./app/tests/file_operation/test.png', "rb"), "image/jpeg")},
            'response': 200
        },
    ]
    for i in range(0, len(files)):
      # reg new user
      response = client.post("auth/sign-up", json=data[i]['request'])
      assert response.status_code == data[i]['response']
      assert isinstance(response.json()['access_token'], str)
      # get token
      token = response.json()['access_token']
      response = client.post("FileOperations/frames", headers={'Authorization': 'Bearer ' + token}, files=files[i]['request'])
      assert response.status_code == files[i]['response']
      # get code
      code = response.json()['result']
      response = client.delete(f"FileOperations/frames/{code}", headers={'Authorization': 'Bearer ' + token})
      assert response.status_code == files[i]['response']
