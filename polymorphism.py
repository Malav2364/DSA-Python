class A:
    def add(self, a, b, c=0, d=0):
        return a + b
    def add(self, a, b, c, d=0):
        return a + b + c
obj = A()
print(obj.add(4, 5, 6)) 
print(obj.add(1, 2, 3, 4)) 
