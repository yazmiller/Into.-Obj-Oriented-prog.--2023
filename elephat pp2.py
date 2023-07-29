from cs1graphics import*
 #from time import sleep 
can=Canvas(500,400)

can.setBackgroundColor("skyblue")

grass=Rectangle(500,80, Point(250,390))
grass.setFillColor('green')
grass.setDepth(100)
can.add(grass)

treetruck=Rectangle(40,200, Point(70,280))
treetruck.setFillColor('brown')
treetruck.setDepth(100)
can.add(treetruck)

treetop=Circle(70,Point(70,150))
treetop.setFillColor('darkgreen')
treetop.setDepth(100)
can.add(treetop)

#start of elephant
elephant=Layer()
elebody=Circle(75, Point(300,270))
elebody.setFillColor('gray')
elebody.setDepth(50)
elephant.add(elebody)

eleleftleg=Rectangle(20,50, Point(260,350))
eleleftleg.setFillColor('gray')
eleleftleg.setDepth(50)
elephant.add(eleleftleg)

elerightleg=Rectangle(20,50, Point(340,350))
elerightleg.setFillColor('gray')
elerightleg.setDepth(50)
elephant.add(elerightleg)

elehead=Circle(45, Point(200,250))
elehead.setFillColor('gray')
elehead.setDepth(50)
elephant.add(elehead)

eletale = Path(Point(410,330),Point(370,270))
eletale.setBorderWidth(6)
elephant.add(eletale)

eleleftear=Circle(25, Point(150,230))
eleleftear.setFillColor('darkgray')
eleleftear.setDepth(100)
elephant.add(eleleftear)

elerightear=Circle(25, Point(250,230))
elerightear.setFillColor('darkgray')
elerightear.setDepth(50)
elephant.add(elerightear)

elelefteye=Circle(5,Point(170,235))
elelefteye.setFillColor('black')
elelefteye.setDepth(50)
elephant.add(elelefteye)

elerighteye=Circle(5,Point(190,245))
elerighteye.setFillColor('black')
elerighteye.setDepth(50)
elephant.add(elerighteye)

elesmile= Path(Point(170,270),Point(190,270))
elephant.add(elesmile)

can.add(elephant)

eletext=Text('Need help getting down?')
eletext.setFontSize(12)
eletext.moveTo(220,190)
can.add(eletext)
#end of elephant
