"""
testing dataclass for my ToDo app
"""

from dataclasses import dataclass

@dataclass
class Todo:
    """Класс для списка задач todo
    """
    id: int
    title: str
    decription: str
    complited: bool
    due_date: str

todo = Todo(1,
            "Купить продукты",
            "Хлеб, молоко, сосиски",
            False,
            "2024-12-30")


print(todo)
print(f"{todo.title}: {todo.decription})

# for i in todo:
    # printf("{i} {data}")