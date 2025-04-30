class shape:
    def area(self):
        print("this is a shape.")

class rectangle(shape):
    def area(self):
        print("this is a rectangle.")

class triangle(shape):
    def area(self):
        print("this is a triangle.")
class square(shape):
    def area(self):
        print("this is a square.")

ob1 = rectangle()
ob2 = triangle()
ob3 = square()

ob1.area()
ob2.area()
ob3.area()
