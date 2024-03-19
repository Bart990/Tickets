class Node:
    """Класс узла, хранит данные и ссылки на предыдущий и следующий узлы."""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    """Класс циклического двусвязного списка."""

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Вставка элемента в начало списка."""
        new_node = Node(data)
        if not self.head:  # Если список пустой
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        """Вставка элемента в конец списка."""
        if not self.head:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = self.head.prev
        self.head.prev.next = new_node
        self.head.prev = new_node

    def delete_from_beginning(self):
        """Удаление элемента из начала списка."""
        if not self.head:
            return
        if self.head.next == self.head:  # Если в списке один элемент
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = self.head.prev.prev
            self.head.prev.next = self.head

    def delete_from_end(self):
        """Удаление элемента из конца списка."""
        if not self.head or self.head.next == self.head:
            self.head = None
        else:
            self.head.prev = self.head.prev.prev
            self.head.prev.next = self.head

    def display(self):
        """Отображение списка."""
        if not self.head:
            print("Список пуст")
            return
        current = self.head
        while True:
            print(current.data, end=' ')
            current = current.next
            if current == self.head:
                break
        print()

    def search(self, key):
        """Поиск элемента по значению."""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:
                break
        return False


# Пример использования
cdll = CircularDoublyLinkedList()
cdll.insert_at_beginning(3)
cdll.insert_at_beginning(2)
cdll.insert_at_end(4)
cdll.insert_at_end(5)
print("Список после вставки элементов:")
cdll.display()  # Вывод: 2 3 4 5

cdll.delete_from_beginning()
print("Список после удаления из начала:")
cdll.display()  # Вывод: 3 4 5

cdll.delete_from_end()
print("Список после удаления с конца:")
cdll.display()  # Вывод: 3 4

print("Поиск значения 4 в списке:", cdll.search(4))  # Вывод: True
print("Поиск значения 1 в списке:", cdll.search(1))  # Вывод: False
