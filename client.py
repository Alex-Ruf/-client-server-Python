import pickle
import time
from functools import wraps
from socket import *
import argparse
import log.client_log_config  as log


def log_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.logger.info(f'Запущена функция: {func.__name__}{args}')
        return func(*args, **kwargs)

    return wrapper


@log_info
def main(client_status: str):
    log.logger.info("Старт программы")
    with init_socket() as soc:

        if client_status == 'r':
            while True:
                msg = receive_message(soc)
                print(f'Получено сообщение {msg}')


        elif client_status == 'w':
            while True:
                msg = input('Ваше сообщение: ')

                if msg == 'exit':
                    soc.close()
                    break
                send_message(soc, msg)


@log_info
def receive_message(s):
    data = pickle.loads(s.recv(1024))
    log.logger.info(f'info: Клиент получил сообщение {data}')
    return data


@log_info
def send_message(soc, msg):
    message = {
        "action": "presence",
        "time": time.time(),
        "user": {
            "account_name": "C0deMaver1ck",
            "message": msg
        }
    }

    soc.send(pickle.dumps(message))
    log.logger.info(f'info: Клиент отправил сообщение.')


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
        while True:
            status = (input('Ваш статус пользователя : писать (w) или читать(r), выход (exit)')).lower()
            if status == 'r' or status == 'w':
                main(status)
                break
            elif status == 'exit':
                break

    except Exception as e:
        log.logger.error(e)
