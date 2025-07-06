"""
Вот идеи для задания №3:

Сделай декоратор retry, который повторяет вызов функции N раз, если она выбрасывает исключение.
Аргументы: @retry(n=3, delay=1)

Пример:

python
Копировать
Редактировать
@retry(n=3, delay=1)
def sometimes_fail():
    if random.random() < 0.7:
        raise ValueError("Неудача")
    return "Успех"
"""

import random
import time
from functools import wraps
from typing import Any


def retry(repeat_count: int, delay_time: int, errors: tuple = (Exception,)):
    """
    Декоратор обеспечивает заданное repeat_count (int) количество повторов
    при указанной задержке delay_time(int) оборациваемой
    функции если она выбрасывает исключения, передаваемые в
      кортеже errors(tuple), по умолчанию Exception

    Аргументы:
    repeat_count(int): количество повтроров выполнения функции, если она
      выбрасывает исключение
    delay_time(int): Время задержки при выполнении оборачивемой функции
    errors (tuple): Обабатываемые исключения (по умолчанию Exception)
    """

    def decorator_retry(func):
        @wraps(func)
        def decorator_wrapper(*args, **kwargs):
            last_exception: Any | None = None
            for i in range(1, repeat_count + 1):
                print("Попытка номер ", i)
                try:
                    return func(*args, **kwargs)
                except errors as err:
                    print(f"Ошибка {err}, повтор через {delay_time} секунд")
                    time.sleep(delay_time)
                    last_exception = err
                    continue

            if last_exception is not None:
                raise last_exception

        return decorator_wrapper

    return decorator_retry


@retry(repeat_count=3, delay_time=1)
def sometimes_fail():
    win_number = random.random()
    print(win_number)
    if win_number < 0.7:
        print(f"Неудача: {win_number}")
        raise ValueError("Неудача")
    return "Успех"


print(sometimes_fail())
