#practical 2
#evolution of postfix element
class Stack:
    def __init__(self, item):
        self.lst= []
    def push(self, item):
        self.lst.append(item)
    def pop(self):
        if self.lst:
            return self.lst.pop()
        else:
            print("Stack is empty")
    def peek(self):
        if self.lst:
            return self.lst[-1]
        else:
            print("Stack is empty")
def evaluate_postfix(expression):
    stack = Stack()
    operators = set(["+", "-", "*", "/"])
    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        elif token in operators:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == "+":
                stack.push(val1 + val2)
            elif token == "-":
                stack.push(val1-val2)
            elif token ==  "*":
                stack.push(val1 * val2)
            elif token == "/":
                stack.push(val1 / val2)
            else:
                raise ValueError(f"invalid token : {token}")
    return stack.pop()

postfix_expression = "9 3 + 5  *"
result  = evaluate_postfix(postfix_expression)
print(f"Result of '{postfix_expression}' is '{result}'")