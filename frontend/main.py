from fastapi import FastAPI
import requests
from google.auth.transport.requests import Request
from google.oauth2 import id_token


def make_open_id_connect_token(client_id):
    open_id_connect_token = id_token.fetch_id_token(Request(), client_id)
    return open_id_connect_token


app = FastAPI()
token = make_open_id_connect_token("111111111111-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com")
headers = {
    "Authorization": f"Bearer {token}",
}


@app.get("/")
def read_root():
    response = requests.get('https://fastapi-sample-backend-dot-my-project-name.appspot.com/', headers=headers)
    return response.text
