'''
Abstraction: 
1. code simplicity. 
2. Make Internes Easy. 
3. Security Enhance
'''

from abc import ABC, abstractmethod

#! Abstract base class: 
class Vehicle(ABC): 
    @abstractmethod
    def start_engine(self): 
        pass
    
    @abstractmethod
    def stop_engine(self): 
        pass
    
#! subclass inheriting Vehicle
class Car(Vehicle): 
    def start_engine(self):
        print("Car engine Start.")
    
    def stop_engine(self):
        print("Car engine stopped.")

#! Subclass inheriting Vehicle. 
class Bike(Vehicle): 
    def start_engine(self):
        print("Bike engine Start.")
    
    def stop_engine(self):
        print("Bike engine stopped.")
        
#! Create Instance and call methods:
car = Car()
car.start_engine()
car.stop_engine()

bike = Bike()
bike.start_engine()
bike.stop_engine()


'''
Vehicle is an abstract class, with start_engine ans stop_engine methods define as abstract methods.
'''