import pickle
from functools import wraps
from socket import *
import argparse
import log.server_log_config as log
import select


def log_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.logger.info(f'Запущена функция: {func.__name__}{args}')
        return func(*args, **kwargs)

    return wrapper


@log_info
def read_requests(r_clients, all_clients):
    responses = {}

    for sock in r_clients:
        try:
            data = pickle.loads(sock.recv(1024))
            responses[sock] = data
            print(f"получено сообщение на сервер")

        except:
            print('Клиент {} {} отключился от сервера'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return responses


@log_info
def write_responses(requests, w_clients, all_clients):
    for sock in w_clients:
        for soc in requests:
            try:
                msg = requests[soc]["user"]["message"]
                sock.send(pickle.dumps(msg))
                print(f"Отправлено сообщение: {msg}")
            except:  # Сокет недоступен, клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


@log_info
def main():
    clients = []

    while True:

        try:
            conn, addr = soc.accept()
            print(addr)
        except OSError as e:
            log.logger.error(e)
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)


        finally:
            # Проверить наличие событий ввода-вывода
            wait = 1
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass

            requests = read_requests(r, clients)
            if requests:
                write_responses(requests, w, clients)


@log_info
def init_socket(addr, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((addr, port))
    s.listen(5)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.settimeout(1)
    log.logger.info(f'Сервер активирован {addr, port}')
    return s


@log_info
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", dest='addr')
    parser.add_argument("-p", dest='port', type=int)
    args = parser.parse_args()
    log.logger.info(f'Получение настроек сервера {args}')
    return args


if __name__ == '__main__':

    try:
        log.logger.info("Старт сервера")
        args = parse_args()
        soc = init_socket(args.addr, args.port)
        main()
    except Exception as e:
        log.logger.error(e)
