stack = []

def push(val):
    stack.append(val)
    print("Pushed:", val)
push(10)
push(20)
push(30)

def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print("Popped:", stack.pop())
pop()

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack:", stack[::-1])
display()

def reverse_string(s):
    temp = []
    for ch in s:
        temp.append(ch)
    rev = ""
    while len(temp) > 0:
        rev += temp.pop()
    print("Reversed string:", rev)
reverse_string("PYTHON")

def reverse_stack():
    temp = []
    while len(stack) > 0:
        temp.append(stack.pop())
    while len(temp) > 0:
        stack.append(temp.pop())
    print("Reversed stack:", stack)
reverse_stack()
