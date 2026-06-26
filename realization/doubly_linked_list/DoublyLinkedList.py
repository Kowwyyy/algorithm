
class DoublyLinkedList:
    class _Node:
        def __init__(self, value, linked_list):
            self._value = value
            self._prev = None
            self._next = None
            self._linked_list = linked_list
            self._is_removed_flag = False

        def get_value(self):
            return self._value

        def _is_removed(self):
            return self._is_removed_flag

        def _mark_as_removed(self):
            self._is_removed_flag = True

        def _belongs_to(self, linked_list):
            return self._linked_list is linked_list

        def __repr__(self): 
            return f"Node(value={self._value})"

    def __init__(self):
        self._head = None
        self._tail = None

    def add_first(self, value):
        new_node = self._Node(value, self)
        if self._is_empty():
            self._initialize(new_node)
        else:
            new_node._next = self._head
            self._head._prev = new_node
            self._head = new_node
        return new_node

    def add_last(self, value):
        new_node = self._Node(value, self)
        if self._is_empty():
            self._initialize(new_node)
        else:
            new_node._prev = self._tail
            self._tail._next = new_node
            self._tail = new_node
        return new_node

    def remove_first(self):
        if self._is_empty():
            raise IndexError("Cannot remove an element from an empty list")

        removed_node = self._head

        if self._has_one_node():
            self._reset()
        else:
            new_head = self._head._next
            self._head._next = None
            new_head._prev = None
            self._head = new_head

        removed_node._mark_as_removed()

        return removed_node

    def remove_last(self):
        if self._is_empty():
            raise IndexError("Cannot remove an element from an empty list")

        removed_node = self._tail

        if self._has_one_node():
            self._reset()
        else:
            prev_node = self._tail._prev
            self._tail._prev = None
            prev_node._next = None
            self._tail = prev_node

        removed_node._mark_as_removed()

        return removed_node

    def remove(self, node):
        if self._is_empty():
            raise IndexError("Cannot remove an element from an empty list")

        if node._is_removed():
            raise ValueError("Element was removed")

        if not node._belongs_to(self):
            raise ValueError("Element does not belong to this list")

        if node == self._head:
            self.remove_first()
            return

        if node == self._tail:
            self.remove_last()
            return

        prev_node = node._prev
        next_node = node._next

        node._prev = None
        node._next = None
        prev_node._next = next_node
        next_node._prev = prev_node

        node._mark_as_removed()

    def _has_one_node(self):
        return self._head == self._tail

    def _reset(self):
        self._head = self._tail = None

    def _is_empty(self):
        return self._head is None

    def _initialize(self, node):
        self._head = self._tail = node
