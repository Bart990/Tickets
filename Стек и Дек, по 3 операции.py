class Stack:
    """Класс стека для хранения элементов."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавление элемента на вершину стека."""
        self.items.append(item)

    def pop(self):
        """Удаление и возвращение элемента с вершины стека."""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """Получение элемента с вершины стека без его удаления."""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Проверка стека на пустоту."""
        return len(self.items) == 0


class Deque:
    """Класс дека для хранения элементов."""

    def __init__(self):
        self.items = []

    def add_front(self, item):
        """Добавление элемента в начало дека."""
        self.items.insert(0, item)

    def add_rear(self, item):
        """Добавление элемента в конец дека."""
        self.items.append(item)

    def is_empty(self):
        """Проверка дека на пустоту."""
        return len(self.items) == 0


# Пример использования стека
stack = Stack()
stack.push(1)
stack.push(2)
print("Вершина стека:", stack.peek())  # Вывод: Вершина стека: 2
print("Удаление из стека:", stack.pop())  # Вывод: Удаление из стека: 2

# Пример использования дека
deque = Deque()
deque.add_front(1)
deque.add_rear(2)
print("Пуст ли дек?", deque.is_empty())  # Вывод: Пуст ли дек? False
