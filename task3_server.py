import pickle
from socket import *
import argparse


def main():
    while True:
        client, addr = soc.accept()
        data = pickle.loads(client.recv(1024))

        response = {
            "user": data["user"]['account_name'],
            "response": 200,
            "alert": "Необязательное сообщение/уведомление"
        }
        client.send(pickle.dumps(response))
        client.close()
        print(data)


def init_socket(addr, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((addr, port))
    s.listen(5)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    return s


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", dest='addr')
    parser.add_argument("-p", dest='port', type=int)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    soc = init_socket(args.addr, args.port)

    try:
        main()
    except Exception as e:
        print(e)
