'''
Method Overriding:
*same method in parent and child class both
'''

#! Parent Class: 
class Animal: 
    def sound(self): 
        print("Animal makes sound!.")

#! Child class inheriting Animal: 
class Dog(Animal): 
    def sound(self): #! Overriding the sound method
        print("Dog Barks!.")

#! 
class Cat(Animal): 
    def sound(self): #! Overriding the sound method
        print("Cat Meows!.")

#! Creating Instances
animal = Animal()
dog = Dog()
cat = Cat()

#! Calling sound method for each other: 
animal.sound()
dog.sound()
cat.sound()

