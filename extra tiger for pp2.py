from cs1graphics import*
from time import sleep

can=Canvas(500,400)

can.setBackgroundColor("skyblue")

grass=Rectangle(500,80, Point(250,390))
grass.setFillColor('green')
grass.setDepth(100)
can.add(grass)

tree=Layer()
treetruck=Rectangle(40,200, Point(70,280))
treetruck.setFillColor('brown')
treetruck.setDepth(100)
tree.add(treetruck)

treetop=Circle(70,Point(70,150))
treetop.setFillColor('darkgreen')
treetop.setDepth(100)
tree.add(treetop)

can.add(tree)

#start of tiger
tiger2=Layer()
tigerbody=Rectangle(100,40, Point(250,310))
tigerbody.setFillColor('orange')
tigerbody.setDepth(50)
tiger2.add(tigerbody)

tigerlleg=Rectangle(10,30, Point(210,340))
tigerlleg.setFillColor('orange')
tigerlleg.setDepth(50)
tiger2.add(tigerlleg)

tigerrileg=Rectangle(10,30, Point(290,340))
tigerrileg.setFillColor('orange')
tigerrileg.setDepth(50)
tiger2.add(tigerrileg)

tigerhead=Circle(20,Point(320,300))
tigerhead.setFillColor('orange')
tigerhead.setDepth(50)
tiger2.add(tigerhead)

tiger1strip=Rectangle(5,30, Point(220,305))
tiger1strip.setFillColor('black')
tiger1strip.setDepth(50)
tiger2.add(tiger1strip)

tiger2strip=Rectangle(5,30, Point(250,305))
tiger2strip.setFillColor('black')
tiger2strip.setDepth(50)
tiger2.add(tiger2strip)

tiger3strip=Rectangle(5,30, Point(280,305))
tiger3strip.setFillColor('black')
tiger3strip.setDepth(50)
tiger2.add(tiger3strip)

tigertale = Path(Point(170,285),Point(200,300))
tigertale.setBorderWidth(6)
tiger2.add(tigertale)

tigerleftear =Rectangle(15,10, Point(300,280))
tigerleftear.setFillColor('darkorange')
tiger2.add(tigerleftear)

tigerrightear =Rectangle(15,10, Point(340,280))
tigerrightear.setFillColor('darkorange')
tiger2.add(tigerrightear)

tigerlefteye=Circle(2,Point(310,295))
tigerlefteye.setFillColor('black')
tigerlefteye.setDepth(50)
tiger2.add(tigerlefteye)

tigerrighteye=Circle(2,Point(330,295))
tigerrighteye.setFillColor('black')
tigerrighteye.setDepth(50)
tiger2.add(tigerrighteye)

tigersmile= Path(Point(310,305),Point(330,305))
tiger2.add(tigersmile)

can.add(tiger2)
