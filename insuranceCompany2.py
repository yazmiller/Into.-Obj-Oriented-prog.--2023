from InsuranceCompany import
def getData():
    name = input("What is the name of the insurance company?")
    address = input("What is the address of the insurance company?")
    return name, address
if __name__ == "__main__":
    icName, icAddress = getData()
    IC = InsuranceCompany(icName,icAddress)
    print(IC)
