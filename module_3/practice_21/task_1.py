import time


def timer(count=5):
    res = 0

    def inner_decorator(func):
        nonlocal res

        def wrapper(*args, **kwargs):
            nonlocal res
            for _ in range(count):
                start_time = time.time()
                func(*args, **kwargs)
                end_time = time.time()
                res += end_time - start_time
            res = res / count
            returned_value = func(*args, **kwargs)
            print(f'Среднее время выполнения функции {res} секунд')
            return returned_value
        return wrapper
    return inner_decorator
