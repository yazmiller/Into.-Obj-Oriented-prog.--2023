from cs1graphics import *
c = Canvas(200,300)
c.setBackgroundColor("pink")
layer1 = Layer()
circle1 = Circle(30,Point(-30,-10))
circle1.setFillColor("orange")
sq = Square(20,Point(-20,-5))
sq.setDepth(40)
sq.setFillColor("white")
layer1.add(sq)
rectangle1 = Rectangle(50,70,Point (-30,55))
rectangle1.setFillColor("blue")
layer1.add(circle1)
layer1.add(rectangle1)
c.add(layer1)
c.wait()
layer1.moveTo(100,150)
layer1.adjustReference(0,50)
layer1.rotate(90)
c.wait()
layer1.flip(180)
