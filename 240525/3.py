# Abstraction :- Hides complex implementation details and provides a simple interface.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car is starting...")


c = Car()
c.start_engine()