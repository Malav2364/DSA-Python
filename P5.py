from collections import deque
class ExpressionEvaluationQueue:
    def __init__(self):
        self.operators={'+':1,'-':1,'':2,'/':3,'*':3}
    def precedence(self,operator):
        return self.operators.get(operator,0)
    def infix_to_postfix(self,expression):
        output=deque()
        stack=[]
        for token in expression.split():
            if  token.isdigit():
                output.append(token)
            elif token=='(':
                stack.append(token)
            elif token==')':
                while stack and stack[-1]!='()':
                    output.append(stack.pop())
                    stack.pop()
                else:
                    while stack and self.precedence(stack[-1]>=self.precedence(token)):
                        output.append(stack.pop())
                        stack.append(token)
                        while stack:
                            output.append(stack.pop())
                        return ''.join(output)
infix_expression="3+4*2/(1-5)**2"
evaluator=ExpressionEvaluationQueue()
postfix_expression=evaluator._infix_to_postfix(infix_expression)
print("Result:",postfix_expression)