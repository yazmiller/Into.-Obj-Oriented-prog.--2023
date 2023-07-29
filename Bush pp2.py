from cs1graphics import*
 #from time import sleep 
can=Canvas(500,400)

can.setBackgroundColor("skyblue")

grass=Rectangle(500,80, Point(250,390))
grass.setFillColor('green')
grass.setDepth(100)
can.add(grass)

bushtruck=Rectangle(20,30, Point(400,340))
bushtruck.setFillColor('brown')
bushtruck.setDepth(100)
can.add(bushtruck)

bush=Circle(45,Point(400,290))
bush.setFillColor('darkgreen')
bush.setDepth(100)
can.add(bush)
