#stack implementation
class Stack:
    def __init__(self):
        self.stack = []
#push operation
    def push(self, data):
        self.stack.append(data)
#pop operation
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack is empty"
#to check if stack is emoty or not
    def is_empty(self):
        return len(self.stack) == 0
#top/ peek operation
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
#to find size
    def size(self):
        return len(self.stack)


s = Stack()
s.push(5)
s.push(10)
print(s.pop())       
print(s.top())       
print(s.is_empty())  
