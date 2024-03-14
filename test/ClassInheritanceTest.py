print("Hello Test")

"""
Inheritance Example
"""
# Parent
class Cycles:
    def set_as_assembled(self, is_assembled):
        self.assembled = is_assembled
    
    def get_wheel_count(self):
        return self.wheel_count
    
    def who_am_i(self):
        return 'I am the original function'
    
# Monocycle
class Monocycle(Cycles):
    # Override the parent function with a similar function that behaves differently
    def who_am_i(self):
        return 'I am overriding the parent function'
    wheel_count = 1

# Bicycle
class Bicycle(Cycles):
    wheel_count = 2

# Tricycle
class Tricycle(Cycles):
    wheel_count = 3


# Create Objects
monocycles = Monocycle()
print('monocycles wheels count:', monocycles.get_wheel_count())

cycles = Bicycle()
print('cycles wheels count:', cycles.get_wheel_count())

# We show how the override function work
print('monocycles:', monocycles.who_am_i())
print('cycles:', cycles.who_am_i())