class bird:
    def fly(self):
        print("Bird can fly.")

class sparrow(bird):
    def fly(self):
        print("Sparrow flies at low height.")
class eagle(bird):
    def fly(self):
        print("eagle flies at very high altitude.")

bird = bird()
sparrow = sparrow()
eagle = eagle()

bird.fly()
sparrow.fly()
eagle.fly()
