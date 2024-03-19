class Stack:
    """Класс реализующий структуру данных стек."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Проверка стека на пустоту."""
        return not self.items

    def push(self, item):
        """Добавление элемента на вершину стека."""
        self.items.append(item)

    def pop(self):
        """Удаление элемента с вершины стека."""
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """Получение элемента с вершины стека без его удаления."""
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Возвращает размер стека."""
        return len(self.items)

    def display(self):
        """Вывод содержимого стека."""
        for item in reversed(self.items):
            print(item)


# Пример использования
stack = Stack()
print("Стек пуст?", stack.is_empty())  # Выводит: True

stack.push(1)  # Добавляем элементы
stack.push(2)
stack.push(3)
print("Верхний элемент стека:", stack.peek())  # Выводит: 3
print("Размер стека:", stack.size())  # Выводит: 3

print("Содержимое стека:")
stack.display()  # Выводит с вершины вниз: 3 2 1

print("Удаленный элемент с вершины стека:", stack.pop())  # Удаляем элемент с вершины
print("Верхний элемент стека после удаления:", stack.peek())  # Выводит: 2
