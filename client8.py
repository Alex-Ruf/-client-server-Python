import pickle
import time
from functools import wraps
from random import random, randint
from socket import *
import argparse
from threading import Thread

import log.client_log_config  as log

room = [""]


def log_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.logger.info(f'Запущена функция: {func.__name__}{args}')
        return func(*args, **kwargs)

    return wrapper


@log_info
def main():
    log.logger.info("Старт программы")
    w_thread = Thread(target=send_message)
    r_thread = Thread(target=receive_message)
    r_thread.daemon = True
    r_thread.start()
    w_thread.start()


@log_info
def receive_message():
    while True:
        try:

            data = pickle.loads(soc.recv(1024))
            if data["room"] == room[-1]:
                log.logger.info(f'info: получено сообщение {data}')
                print(f'Сообщение от {data["user"]["account_name"]}: {data["user"]["message"]}')

        except OSError as e:
            log.logger.error(e)


@log_info
def send_message():
    print(f'Действия:n - new name, r - room, q - exit room.')
    name = "C0deMaver1ck"
    while True:

        try:
            print(f'Info- Room: {room[-1]} , User: {name}')
            msg = input()
            if msg == 'exit':
                soc.close()
                break
            if msg == 'r':
                room.append(input('Номер комнаты '))
            elif msg == 'q':
                if len(room)>1:
                    del room[-1]
            elif msg=='n':
                name=input('New name:')
            else:
                message = {
                    "action": "presence",
                    "time": time.time(),
                    "room": room[-1],
                    "user": {
                        "account_name": name,
                        "message": msg}}

                soc.send(pickle.dumps(message))
                log.logger.info(f'info: Клиент отправил сообщение.')
        except Exception as e:
            log.logger.error(e)


@log_info
def init_socket():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default='127.0.0.1')
    parser.add_argument('port', type=int, default='3456')
    args = parser.parse_args()
    s = socket(AF_INET, SOCK_STREAM)
    # s.connect(('127.0.0.1', 5678))
    s.connect((args.addr, args.port))
    log.logger.info(f'info: Клиент подключился к серверу {args.addr, args.port} ')
    return s


if __name__ == '__main__':
    try:
        soc = init_socket()

        main()

    except Exception as e:
        log.logger.error(e)
