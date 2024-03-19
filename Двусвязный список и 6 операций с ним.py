class Node:
    """Класс узла, содержит данные и ссылки на предыдущий и следующий узлы."""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Класс двусвязного списка."""

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Вставка элемента в начало списка."""
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        """Вставка элемента в конец списка."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_from_beginning(self):
        """Удаление элемента из начала списка."""
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    def delete_from_end(self):
        """Удаление элемента с конца списка."""
        if self.head is None:
            return
        last = self.head
        while last.next:
            last = last.next
        if last.prev is not None:
            last.prev.next = None
        else:  # Список состоял из одного элемента
            self.head = None

    def search(self, key):
        """Поиск элемента по значению."""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        """Отображение списка."""
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()


# Пример использования
dll = DoublyLinkedList()
dll.insert_at_beginning(1)
dll.insert_at_beginning(2)
dll.insert_at_end(3)
dll.insert_at_end(4)
print("Список после вставки элементов:")
dll.display()  # Выведет: 2 1 3 4

dll.delete_from_beginning()
print("Список после удаления из начала:")
dll.display()  # Выведет: 1 3 4

dll.delete_from_end()
print("Список после удаления с конца:")
dll.display()  # Выведет: 1 3

print("Поиск значения 3 в списке:", dll.search(3))  # Выведет: True
print("Поиск значения 5 в списке:", dll.search(5))  # Выведет: False
