from client import *

def test_receive_message():
    data = {
        "user": 'User',
        "response": 200,
        "alert": "Необязательное сообщение/уведомление"
    }

    assert receive_message(data) == 'Сообщение от сервера: Пользователь-User, статус соединения 200'

