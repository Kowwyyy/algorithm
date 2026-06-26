class ArrayStack:
    def __init__(self, initial_capacity = 10):
        self._capacity= initial_capacity
        self._value = [None] * self._capacity
        self._index = 0

    def is_empty(self):
        return self._index == 0
    
    def size(self):
        return self._index

    def _resize(self):
        new_capacity = int(self._capacity * 1.5) + 1
        new_values= [None] * new_capacity

        for i in range(self._value):
            new_values[i] = self._value[i]

        self._value = new_values
        self._capacity = new_capacity

    def push(self, value):
        if self._index == self._capacity:
            self._resize()
        self._value[self._index] = value
        self._index += 1
     
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        
        self._index -= 1
        value = self._value[self._index]
        self._value[self._index] = None

        return value
    
    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')

        return self._value[self._index - 1]
    
    def __str__(self):
        return str(self._value[ : self._index])
    


