# from collections import deque

# class ExpressionEvaluatorQueue:
#     def __init__(self):
#         self.operators = {'+':1,'-':1,'*':2,'/':2,'**':3}

#     def precedence(self,operator):
#         return self.operators.get(operator,0)


#     def _infix_to_postfix(self,expression):
#         output = deque()
#         stack = []
#         for token in expression.split():
#             if token.isdigit():
#                 output.append(token)
#             elif token == '(':
#                 stack.append(token)
#             elif token == ')':
#                 while stack and stack[-1] != '(':
#                     output.append(stack.pop())
#                 stack.pop() 
#             else:
#                 while stack and self.precedence(stack[-1]) >= self.precedence(token):
#                     output.append(stack.pop())
#                 stack.append(token)
#         while stack:
#             output.append(stack.pop())
#         return ' '.join(output)

# infix_expression = "3 + 4 * 2 / ( 1 - 5 ) ** 2"
# evaluator = ExpressionEvaluatorQueue()
# postfix_expression = evaluator._infix_to_postfix(infix_expression)
# print("Result:", postfix_expression)





# # import queue

# # class PostfixEvaluator:
# #     def __init__(self, expression):
# #         self.expression = expression

# #     def _precedence(self, operator):
# #         if operator == '+' or operator == '-':
# #             return 1
# #         elif operator == '*' or operator == '/':
# #             return 2
# #         elif operator == '**':
# #             return 3
# #         else:
# #             return 0


# #     def _infix_to_postfix(self):
# #         output = []
# #         stack = []
# #         for token in self.expression.split():
# #             if token.isdigit():
# #                 output.append(token)
# #             elif token == '(':
# #                 stack.append(token)
# #             elif token == ')':
# #                 while stack and stack[-1] != '(':
# #                     output.append(stack.pop())
# #                 stack.pop() 
# #             else:
# #                 while stack and self.precedence(stack[-1]) >= self.precedence(token):
# #                     output.append(stack.pop())
# #                 stack.append(token)
# #         while stack:
# #             output.append(stack.pop())
# #         return ' '.join(output)

# # infix_expression = "3 + 4 * 2 / ( 1 - 5 ) ** 2"
# # postfix_evaluator = PostfixEvaluator(infix_expression)
# # print("Result:", postfix_evaluator._infix_to_postfix())

class Priority_Q:
    def __init__(self):
        self.q=[]
    def enqueue(self,data, priority):
        index=0
        while index<len(self.q) and self.q[index][1]>=priority:
            index+=1
        self.q.insert(index,(data,priority))
    def dequeue(self):
        if self.q:
            return self.q.pop(0)
        else:
            print("Queue is empty")
    
    def pr(self):
        if len(self.q)<3:
            print("Queue does not contain 3 element")
        else:
            product=1
            for i in range(3):
                product*=(self.q[i][0])
            print("Product of 3 largest distinct number is :",product)
    def display(self):
        if self.q:
            print(self.q)
        else:
            print("Queue is empty")

q=Priority_Q()
q.enqueue(1,1)
q.enqueue(2,2)
q.enqueue(3,3)
q.enqueue(4,4)
q.enqueue(5,5)
q.display()
q.product()