from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def cat(self):
        print("Meow")
class B(A):
    def dog(self):
        print("Woof")
d1=B()