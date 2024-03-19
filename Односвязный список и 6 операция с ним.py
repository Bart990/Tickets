class Node:
    """Класс для узла связного списка"""

    def __init__(self, data):
        self.data = data  # Данные узла
        self.next = None  # Ссылка на следующий узел


class LinkedList:
    """Класс для связного списка"""

    def __init__(self):
        self.head = None  # Начальный узел списка

    def is_empty(self):
        """Проверка списка на пустоту"""
        return self.head is None

    def append(self, data):
        """Добавление элемента в конец списка"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert(self, prev_node, data):
        """Вставка элемента после указанного узла"""
        if not prev_node:
            print("Указанный предыдущий узел должен существовать.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        """Удаление узла по значению"""
        temp = self.head

        # Если удаляемый узел является головным
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Поиск удаляемого узла
        while temp and temp.next and temp.next.data != key:
            temp = temp.next

        if temp is None or temp.next is None:
            return

        # Удаление узла из списка
        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self, key):
        """Поиск элемента по значению"""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def print_list(self):
        """Печать всех элементов списка"""
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def delete_list(self):
        """Удаление всего списка"""
        self.head = None


# Пример использования
if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.print_list()  # Печать списка
    llist.insert(llist.head.next, 5)  # Вставка элемента после второго узла
    llist.print_list()
    print("Элемент найден:", llist.search(3))  # Поиск элемента
    print("Элемент найден:", llist.search(10))  # Поиск элемента
    llist.delete_node(2)  # Удаление элемента
    llist.print_list()
    print("Список пустой:", llist.is_empty())  # Проверка на пустоту
    llist.delete_list()  # Удаление списка
    print("Список пустой после удаления:", llist.is_empty())
