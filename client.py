import pickle
import time
from functools import wraps
from socket import *
import argparse
import log.client_log_config  as log


def log_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.info(f'Запущена функция: {func.__name__}{args}')
        return func(*args, **kwargs)
    return wrapper

@log_info
def main():
    log.main("Старт программы")
    soc = init_socket()
    send_message(soc)
    receive_message(soc)
    soc.close()

@log_info
def receive_message(s):
    data = pickle.loads(s.recv(1024))
    a= (f'Сообщение от сервера: Пользователь-{data["user"]}, статус соединения {data["response"]}')
    log.info(f'info: Клиент получил сообщение {a}')
    print( a)

@log_info
def send_message(soc):
    msg= {
            "action": "presence",
            "time": time.time(),
            "user": {
                    "account_name":  "C0deMaver1ck",
                    "status":      "Yep, I am here!"
        }
        }

    soc.send(pickle.dumps(msg))
    log.info(f'info: Клиент отправил сообщение: {msg}')

@log_info
def init_socket():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default='127.0.0.1')
    parser.add_argument('port', type=int,default='3456')
    args = parser.parse_args()
    s = socket(AF_INET, SOCK_STREAM)
    # s.connect(('127.0.0.1', 3456))
    s.connect((args.addr, args.port))
    log.info(f'info: Клиент подключился к серверу {args.addr, args.port} ')
    return s



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log.errore(e)



