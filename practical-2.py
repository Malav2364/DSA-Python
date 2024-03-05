#practical 2 
# Evaluation of postfix expression 

class Stack: 
    def __init__(self):
        self.lst=[]
    def push(self,item):
        self.lst.append(item)
    def pop(self): 
        if self.lst:
            return self.lst.pop()
        else:
            print("stack is empty")
    def is_empty(self):
        return len(self.lst)==0
    def peek(self):
        if self.lst:
            return self.lst[-1]
        else:
            print("Stack is empty")
def evaluate_postfix(expression):
    stack=Stack()
    operators=set(["+","-","*","/"])
    
    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        elif token in operators:
            val2=stack.pop()
            val1=stack.pop()
            if token=="+":
                stack.push(val1+val2)
            elif token=="-":
                stack.push(val1-val2)
            elif token=="*":
                stack.push(val1*val2)
            elif token=="/":
                stack.push(val1/val2)
            else:
                raise ValueError("invalid token: {token}")
    return stack.pop()

postfix_expression="9 3 + 5 *"
result=evaluate_postfix(postfix_expression)
print(f"result of {postfix_expression}={result}")