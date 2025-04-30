class animal:
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print("dog says: barking.")

class cat(animal):
    def sound(self):
        print("cat says: meow meow.")

class cow(animal):
    def sound(self):
        print("cow says: moo maa.")

animals = [dog(), cat(), cow()]

for animal in animals:
    animal.sound()