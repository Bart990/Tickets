class Deque:
    """Класс реализующий структуру данных дек."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Проверка дека на пустоту."""
        return not self.items

    def add_front(self, item):
        """Добавление элемента в начало дека."""
        self.items.insert(0, item)

    def add_rear(self, item):
        """Добавление элемента в конец дека."""
        self.items.append(item)

    def remove_front(self):
        """Удаление элемента из начала дека."""
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        """Удаление элемента из конца дека."""
        if self.items:
            return self.items.pop()
        return None

    def size(self):
        """Возвращает размер дека."""
        return len(self.items)


# Пример использования
deque = Deque()
print("Дек пуст?", deque.is_empty())  # Выводит: True

deque.add_front(1)  # Добавляем элемент в начало
deque.add_rear(2)  # Добавляем элемент в конец
print("Размер дека после добавления элементов:", deque.size())  # Выводит: 2

print("Удаленный элемент из начала:", deque.remove_front())  # Удаляем элемент из начала
print("Удаленный элемент из конца:", deque.remove_rear())  # Удаляем элемент из конца
print("Размер дека после удаления элементов:", deque.size())  # Выводит: 0
