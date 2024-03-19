class Node:
    """Класс для узла циклического связного списка"""

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    """Класс для циклического связного списка"""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Добавление элемента в конец списка"""
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def print_list(self):
        """Печать всех элементов списка"""
        if self.head:
            current = self.head
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    break
            print()

    def is_empty(self):
        """Проверка списка на пустоту"""
        return not self.head

    def delete_node(self, key):
        """Удаление узла по значению"""
        if self.head:
            if self.head.data == key and self.head.next == self.head:
                self.head = None
                return
            current = self.head
            prev = None
            while True:
                if current.data == key:
                    if prev:
                        prev.next = current.next
                        if current == self.head:
                            self.head = current.next
                    else:
                        # Если узел является единственным узлом
                        while current.next != self.head:
                            current = current.next
                        current.next = self.head.next
                        self.head = self.head.next
                    return
                prev = current
                current = current.next
                if current == self.head:
                    break

    def search(self, key):
        """Поиск элемента по значению"""
        current = self.head
        while True:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def delete_list(self):
        """Удаление всего списка"""
        self.head = None


# Пример использования
if __name__ == "__main__":
    clist = CircularLinkedList()
    clist.append(1)
    clist.append(2)
    clist.append(3)
    clist.print_list()  # Печать списка
    print("Элемент найден:", clist.search(2))  # Поиск элемента
    print("Элемент найден:", clist.search(200))  # Поиск элемента
    clist.delete_node(2)  # Удаление элемента
    clist.print_list()
    print("Список пустой:", clist.is_empty())  # Проверка на пустоту
    clist.delete_list()  # Удаление списка
    print("Список пустой после удаления:", clist.is_empty())
