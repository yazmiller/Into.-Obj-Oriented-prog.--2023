from cs1graphics import*

can=Canvas(500,300,"grey")

rec=Rectangle(200,100)
rec.moveTo(250,200)
rec.setFillColor("white")
rec.setBorderColor("yellow")
rec.setBorderWidth(5)
can.add(rec)

cir=Circle()
cir.setFillColor("brown")
cir.setRadius(50)
cir.moveTo(350,100)
can.add(cir)

              
