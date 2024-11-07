#! Multiple Inheritance: 
#! Parent Class one: 
class Animal: 
    def eat(self): 
        print("Animal Eats Food!.")
        
#! Parent Class two: 
class Pet: 
    def stay_at_home(self): 
        print("Animal Stays at hone")

#! Child Class inheriting multiple classes 
class Dog(Animal, Pet): 
    def bark(self): 
        print("Dog Barks!.")

dog = Dog()
dog.eat()  #! inherit from Animal class
dog.stay_at_home() #! inherit from Pet class
dog.bark() #! inherit from Dog child Class