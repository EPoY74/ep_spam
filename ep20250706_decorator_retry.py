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

    @wraps
    def decorator_retry(func):
        def decorator_wrapper(*args, **kwargs):
            result: Any | None = None

            return result

        return decorator_wrapper

    return decorator_retry


def sometimes_fail():
    if random.random() < 0.7:
        raise ValueError("Неудача")
    return "Успех"
