import pickle
from functools import wraps
from socket import *
import argparse
import log.server_log_config as log


def log_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.info(f'Запущена функция: {func.__name__}{args}')
        return func(*args, **kwargs)
    return wrapper

@log_info
def main():
    while True:
        client, addr = soc.accept()
        data = pickle.loads(client.recv(1024))
        log.info(f'Подключен клиент и получено сообщение {data["user"]["account_name"]}')

        response = {
            "user": data["user"]['account_name'],
            "response": 200,
            "alert": "Необязательное сообщение/уведомление"
        }
        client.send(pickle.dumps(response))
        log.info(f'Отправлено сообщение {response}')
        client.close()
        print(data)
        log.info(f'Отключение от клиента {data["user"]["account_name"]}')

@log_info
def init_socket(addr, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((addr, port))
    s.listen(5)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    log.info(f'Сервер активирован {addr,port}')
    return s

@log_info
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", dest='addr')
    parser.add_argument("-p", dest='port', type=int)
    args = parser.parse_args()
    log.info(f'Получение настроек сервера {args}')
    return args


if __name__ == '__main__':

    try:
        log.main("Старт сервера")
        args = parse_args()
        soc = init_socket(args.addr, args.port)
        main()
    except Exception as e:
        log.errore(e)
