import os
import time


def log_usage(func):
    def wrapper(*args, **kwargs):
        try:
            with open(os.path.join('logs', f'usage_{func.__name__}'),
                      "x") as file:
                print(time.ctime(time.time()), file=file)
        except FileExistsError:
            with open(os.path.join('logs', f'usage_{func.__name__}'),
                      "a") as file:
                print(time.ctime(time.time()), file=file)
        return func(*args, **kwargs)

    return wrapper
