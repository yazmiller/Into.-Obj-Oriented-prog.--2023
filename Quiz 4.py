from cs1graphics import*

can=Canvas(600,400,"lightblue")

snow=Circle()
snow.setRadius(70)
snow.setFillColor("white")
snow.moveTo(300,110)
can.add(snow)

bottomhat=Rectangle(100,30)
bottomhat.moveTo(300,50)
bottomhat.setFillColor("black")
bottomhat.setDepth(40)
can.add(bottomhat)

tophat=Rectangle(50,60)
tophat.moveTo(300,35)
tophat.setFillColor("black")
tophat.setDepth(40)
can.add(tophat)

lefteye=Circle()
lefteye.setRadius(13)
lefteye.setFillColor("darkgrey")
lefteye.moveTo(265,85)
lefteye.setDepth(40)
can.add(lefteye)

righteye=Circle()
righteye.setRadius(13)
righteye.setFillColor("darkgrey")
righteye.moveTo(330,85)
righteye.setDepth(40)
can.add(righteye)

nose= Polygon(Point(400,100), Point(295,100), Point(295,129))
nose.setFillColor('orange')
nose.setDepth(40)
can.add(nose)

smile = Circle(50, Point(300,100))
smile.setFillColor('black')
smile.setDepth(50)
can.add(smile)

smileCover = Circle(55, Point(300,90))
smileCover.setFillColor('white')
smileCover.setBorderWidth(0)
smileCover.setDepth(50)
can.add(smileCover)

body=Circle()
body.setRadius(90)
body.setFillColor('white')
body.moveTo(300,250)
body.setDepth(60)
can.add(body)

armLeft = Path(Point(150,160),Point(250,240))
can.add(armLeft)

armRight = Path(Point(350,240),Point(450,160))
can.add(armRight)

words=Text("Click snowman to make him frown")
words.setFontSize(20)
words.moveTo(300,353)
can.add(words)

frown = Circle(50, Point(300,180))
frown.setFillColor('black')
frown.setDepth(50)
can.add(frown)

frownCover = Circle(55, Point(300,200))
frownCover.setFillColor('white')
frownCover.setBorderWidth(0)
frownCover.setDepth(50)
can.add(frownCover)




