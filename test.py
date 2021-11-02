from werkzeug.wrappers import response
from app import app 

def test1():
    response = app.test_client().get("/")
    assert response.status_code==200


def test2():
    response = app.test_client().get("/")
    assert b"Wyorld" in response.data 