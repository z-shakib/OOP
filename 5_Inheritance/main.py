'''
Inheritance: 
1. Code Reusability. 
2. Code Organization. 
3. Functionality Enhancement.
'''

#! Parent Class:
class Animal: 
    def __init__(self, name):
        self.name = name

    def speak(self): 
        print(f"{self.name} make a sound.")
        
#! Child Class, Inheriting Animal.
class Dog(Animal): 
    def speak(self): 
        print(f"{self.name} says Woof!")

dog = Dog('Buddy')
dog.speak()
