list=[]
number=int(input("Enter a 1-10"))
list.append(number)
number=int(input("Enter a 1-10"))
list.append(number)
number=int(input("Enter a 1-10"))
list.append(number)
number=int(input("Enter a 1-10"))
list.append(number)
number=int(input("Enter a 1-10"))
list.append(number)

print("The rating given were",list[0],list[1],list[2],list[3],list[4])
highest=max(list)
print(highest)
lowest=min(list)
print(lowest)
average=len(list)
print(average)
