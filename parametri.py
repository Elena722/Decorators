import logging
import random
import functools
from datetime import datetime

def quadratic(a,b,c):
    def wrapper(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            x = func(*args, **kwargs)
            res = a*(x**2) + b*x + c
            # print(f'x={x}, {res}')
            logging.info(f'(x={x}, result={res})')
            return res
        return wrap
    return wrapper

@quadratic(1, 2, 3)
def random_x():
    x = random.randint(1, 100)
    # x = 1
    return x

if __name__ == "__main__":
    l = logging.getLogger()  # root (l - logger)
    l.setLevel(logging.DEBUG)  # root
    # create console handler and set level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(logging.Formatter("%(levelname)s -> line %(lineno)d -> %(message)s"))
    l.addHandler(console_handler)

    x = datetime.now()
    filename = str(x.date()) + '-quadratic.log'

    file_handler = logging.FileHandler(filename, 'w+')
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(logging.Formatter("%(levelname)s (%(asctime)s) -> %(filename)s, (line %(lineno)d) -> %(message)s"))
    l.addHandler(file_handler)

    for i in range(100):
        if random_x() > 600:
            logging.error('Result too much')
