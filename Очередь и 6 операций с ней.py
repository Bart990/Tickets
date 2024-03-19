class Queue:
    """Класс реализующий структуру данных очередь."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Проверка очереди на пустоту."""
        return not self.items

    def enqueue(self, item):
        """Добавление элемента в очередь."""
        self.items.append(item)

    def dequeue(self):
        """Удаление элемента из очереди."""
        if self.items:
            return self.items.pop(0)
        return None

    def peek(self):
        """Получение первого элемента очереди без его удаления."""
        if self.items:
            return self.items[0]
        return None

    def size(self):
        """Возвращает размер очереди."""
        return len(self.items)

    def display(self):
        """Вывод содержимого очереди."""
        for item in self.items:
            print(item, end=' ')
        print()


# Пример использования
queue = Queue()
print("Очередь пуста?", queue.is_empty())  # Выводит: True

queue.enqueue(1)  # Добавляем элементы
queue.enqueue(2)
queue.enqueue(3)
print("Первый элемент очереди:", queue.peek())  # Выводит: 1
print("Размер очереди:", queue.size())  # Выводит: 3

print("Содержимое очереди:")
queue.display()  # Выводит: 1 2 3

print("Удаленный элемент из очереди:", queue.dequeue())  # Удаляем элемент
print("Первый элемент очереди после удаления:", queue.peek())  # Выводит: 2
