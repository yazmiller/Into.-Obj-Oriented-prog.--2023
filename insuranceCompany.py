class InsuranceCompany:
    def __init__(self,n,a):
        self.iname = n
        self._Iaddress = a
    def getName(self):
        return self._Iname
    def getAddress(self):
        return self._Iaddress
    def setName (self,a):
        self.Iname = n
    def setAddress(self,a):
        self._Iaddress = a
    def __str__(Self):
        s = self.+Iname
        st+ "   "
        st = self.Iaddress
        return s

if __name__ == "__main__":
    insurance = InsuranceCompany("Aetna", "1 River St.")
    print(insurance.getName())
    insurance.setName("Life")
    print(insurance)
        
    
