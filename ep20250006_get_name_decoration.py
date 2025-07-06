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


def log_call(func):
    """
    Декоратор для вывода на экран имени функции,
    переданных ей пареметров и результата.
    """

    @wraps
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(f"Вызов {func.__name__}. Переданные аргуименты: {args}, {kwargs}")
        print(f"Результат: {func(*args, **kwargs)}")
        return func(*args, **kwargs)

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

    return a + b


# print(add(2, 2))
add(2, 2)
