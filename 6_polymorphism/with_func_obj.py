class Dog: 
    def speak(self): 
        return "Dog makes sound like, woof!"

class Cat: 
    def speak(self): 
        return "Cat makes sound like, Meow"

#! Function that takes any object and calls its speak method
def animal_sound(animal): 
    print(animal.speak())

#! Creating Instances: 
dog = Dog()
cat = Cat()

#! calling the function with different objects: 
animal_sound(dog)
animal_sound(cat)
