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

    def is_empty(self):
        """Проверка стека на пустоту."""
        return len(self.items) == 0


class Queue:
    """Класс очереди для хранения элементов."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Добавление элемента в конец очереди."""
        self.items.append(item)

    def dequeue(self):
        """Удаление и возвращение элемента из начала очереди."""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        """Проверка очереди на пустоту."""
        return len(self.items) == 0


# Пример использования стека
stack = Stack()
stack.push('a')
stack.push('b')
print("Стек пуст?", stack.is_empty())  # Выведет: False
stack.pop()

# Пример использования очереди
queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
print("Очередь пуста?", queue.is_empty())  # Выведет: False
queue.dequeue()
