from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def hello(self,name):
        print(f"Hello! {name}")
class Child(Parent):
    def hello(self,name):
        print(f"Hello! {name}")
    def welcome(self):
        print("Welcome")

s = Child()
s.welcome()
s.hello("Kal")