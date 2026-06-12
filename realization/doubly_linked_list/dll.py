class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None 
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None # Начальный (первый) узел
        self.tail = None # Конечный (последний) узел

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # Если список пуст
            self.head = self.tail = new_node  # Первый элемент — и голова, и хвост
        else:
            self.tail.next = new_node  # Связываем текущий хвост с новым узлом
            new_node.prev = self.tail  # Связываем новый узел с текущим хвостом
            self.tail = new_node  # Обновляем хвост

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:  
            self.head = self.tail = new_node  
        else:
            new_node.next = self.head  # Новый узел указывает на текущую голову
            self.head.prev = new_node  # Текущая голова знает, что перед ней новый узел
            self.head = new_node  # Обновляем голову

    def delete(self, data):
        if self.head is None:
            return  # Список пуст

        current = self.head
        while current:
            if current.data == data:
                # Если удаляемый элемент - это голова
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None  # Обнуляем указатель на предыдущий узел у новой головы
                # Если удаляемый элемент - это хвост
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None  # Обнуляем указатель на следующий узел у нового хвоста
                # Если удаляемый элемент находится в середине
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse_traverse(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()    