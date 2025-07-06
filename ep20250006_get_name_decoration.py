"""
Задание от chatgpt:
Вот тебе задача №1:

🔧 Упражнение 1: Оберни функцию логирующим декоратором
Создай декоратор log_calls, который будет:

выводить в консоль имя функции

список аргументов, с которыми она вызвана

результат её выполнения

Пример:

python
Копировать
Редактировать
@log_calls
def add(x, y):
    return x + y

add(2, 3)
Ожидаемый вывод:

csharp
Копировать
Редактировать
Вызов add с аргументами: (2, 3), {}
Результат: 5
"""

from functools import wraps
import time


def log_call(func):
    """
    Декоратор для вывода на экран имени функции,
    переданных ей пареметров и результата.
    Так же измеряется время выполнения функции с точностью :.4f
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(f"Вызов {func.__name__}. Переданные аргуименты: {args}, {kwargs}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Результат: {result}")
        execution_time = end_time - start_time
        print(
            f"Время выполнения: {execution_time:.4f} секунд",
        )
        return result

    return wrapper


@log_call
def add(a: int, b: int) -> int:
    """
    Сложение двух целых чисел

    Аргументы:
    a(int) - Первое слагаемое
    b(int) - Второе слагаемое

    Результат: int
    """
    time.sleep(0.5)
    return a + b


# print(add(2, 2))
add(2, 2)
