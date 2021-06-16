import datetime
import inspect

from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = inspect.stack()
        print(f'{datetime.datetime.now()} Функция {func.__name__}() вызвана из функции {func_name[1][3]} ')
        return func(*args, **kwargs)
    return wrapper

@log
def func_z():
    pass

def main():
 func_z()

if __name__ == '__main__':
    main()