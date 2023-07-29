from cs1graphics import*

can=Canvas(600,400,"lightblue")

righteyeCir=Circle()
righteyeCir.setRadius(30)
righteyeCir.setFillColor("darkgrey")
righteyeCir.moveTo(50,50)
can.add(righteyeCir)










righteye=Circle()
righteye.setRadius(30)
righteye.setFillColor("darkgrey")
righteye.moveTo(50,50)
can.add(righteye)

nose=Polygon(Point(),Point(),Point())
nose.setFillColor("lightorange")
can.add(nose)

smile=Path(Point(),Point())
