def getData():
    name = input("Enter your name")
    password = input("Enter your password")
    return name, password
if __name__== "__main__":
    name,password = getData()
    print("Name is",name,"Password is",password)
