from cs1graphics import *
paper = Canvas()
paper.set backgroundColor('skyBlue')
paper.setWidth(300,200)

#make sun
sun.move(250, 50)
sun.setRadius(30)
sun.setFillColor('yellow')
#make house 
façade = Square(60, Point(140, 130))
façade.setFillColor('white')
paper.add(façade)
#make chimney
chimney = Rectangle(15, 18, Point(155, 85))
chimney.setFillColor('red')
paper.add(chimney)
#make tree
tree = Polygon(Point(50,80), Point(30,140), Point(70, 140))
tree.setFillColor('darkGreen')
paper.add(tree)
