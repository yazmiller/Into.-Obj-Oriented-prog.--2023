rate = float(input("Enter the loan's rate "))
r = (rate/100)/12
r = round(r,9)
P= float (input("Enter the principal amount of the loan "))
Years = int(input("Enter the number of years (the term)"))
N= (Years * 12)
c =(r*P)/(1-(pow(1+r,-N)))
print ("Your monthly payment is", round(c,2))
