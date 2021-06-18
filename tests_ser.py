from server import *



def test_response():
    assert response('C0deMaver1ck')=={"user": 'C0deMaver1ck',"response": 200,"alert": "Необязательное сообщение/уведомление"}