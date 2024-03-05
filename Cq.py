#program to find NGE element from an array 

class NextgreaterelementFinder: 
    def  __init__(self, lst): 
        self.lst=lst 
        self.stack=[]
    def find_next_greater_element(self):
        result=[]
        for i in range(len(self.lst)-1,-1,-1):
            while self.stack and self.lst[i] >= self.stack[-1]:
                self.stack.pop()
            if not self.stack:
                result.append((self.lst[i],-1))
            else:
                result.append((self.lst[i],self.stack[-1]))
                self.stack.append(self.lst[i])
            result.reverse()
        return result
lst=[1,2,4,5,6]
finder=NextgreaterelementFinder(lst)
next_greater_elements=finder.find_next_greater_element()
for element,nextgreater in next_greater_elements:
    print(f"{element} --> {nextgreater}",end=' ')