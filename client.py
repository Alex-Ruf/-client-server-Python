import pickle
import time
from socket import *
import argparse



def main():

    msg= {
            "action": "presence",
            "time": time.time(),
            "user": {
                    "account_name":  "C0deMaver1ck",
                    "status":      "Yep, I am here!"
        }
        }
    send(soc, msg)
    data = pickle.loads(soc.recv(1024))
    print(receive_message(data))

    soc.close()

def receive_message(data):


    a=f'Сообщение от сервера: Пользователь-{data["user"]}, статус соединения {data["response"]}'

    return a
def send(soc, msg):
    soc.send(pickle.dumps(msg))

def init_socket(addr,port):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, port))
    return s


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr')
    parser.add_argument('port', type=int)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    soc = init_socket(args.addr,args.port)

    try:
        main()
    except Exception as e:
        print(e)