"""
Polymorphism
"""

'''
Example 1: Pet
'''
# Parent Object
class Pet:
    def sound(self):
        pass

# Is-A pet
class Cat(Pet):
    def sound(self):
        return "Cat sound"

# Is-A pet
class Dog(Pet):
    def sound(self):
        return "Dog bark"
    

def get_sound(pet: Pet):
    return pet.sound()

print(get_sound(Cat()))
print(get_sound(Dog()))


'''
Example 2 : Quadrilateral
'''

class Quadrilateral:
    def get_area(self):
        pass

class Square(Quadrilateral):
    side = 0

    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side**2
    
class Rectangle(Quadrilateral):
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
def calculate_area(quad : Quadrilateral):
    return quad.get_area()

print(calculate_area(Square(2)))
print(calculate_area(Rectangle(2,3)))



