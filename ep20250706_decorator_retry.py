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


def retry(repeat_count: int, delay_time: int):
    """
    Декоратор обеспечивает заданное repeat_count (int) количество повторов
    при указанной задержке delay_time(int) оборациваемой
    функции если она выбрасывает исключение

    Аргументы:
    repeat_count(int): количество повтроров выполнения функции, если она
      выбрасывает исключение
    delay_time(int): Время задержки при выполнении оборачивемой функции
    """

    def decorator_retry(func):
        @wraps(func)
        def decorator_wrapper(*args, **kwargs):
            last_exseption: Any | None = None
            for i in range(1, repeat_count + 1):
                print("Попытка номер ", i)
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    time.sleep(delay_time)
                    last_exseption = err
                    continue
            raise Exception(last_exseption)

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
