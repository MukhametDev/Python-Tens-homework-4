class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item, index):
        self.stack.append((item, index))

    def pop(self):
        return self.stack.pop() if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1] if self.stack else None

def check_str(s):
    my_stack = Stack()
    bracket_map = {'(': ')', '{': '}', '[': ']'}
    open_brackets = bracket_map.keys()
    close_brackets = bracket_map.values()

    for i, char in enumerate(s, start=1):
        if char in open_brackets:
            my_stack.push(char, i)
        elif char in close_brackets:
            if my_stack.is_empty():
                return i
            last_open, index = my_stack.pop()
            if bracket_map[last_open] != char:
                return i

    if not my_stack.is_empty():
        return my_stack.pop()[1]

    return "Success"

# Тестирование функции
print(check_str("[{}([])]"))
print(check_str("[()()]("))
