class Policy:
    def __init__(self, num, dat, nam, add, pAmount):
        self._policyNumber = num
        self._policyDate= dat
        self._policyName = nam
        self._policyAddress = add
        self._policyPremium = pAmount
        
    def getNum(self):
        return self._policyNumber
    
    def getNam(self):
        return self._policyName
    
    def getAdd(self):
        return self._policyAddress
    
    def getAmount(self):
        return self._policyPremium
    
    def getDate(self):
        return self._policyDate
    
    def setNum(self, num):
        self._policyNumber = num
        
    def setNam(self, name):
        self._policyName = nam
        
    def setAdd(self, addr):
        self._policyAddress = add
        
    def setAmount(self, premium):
        self._policyPremium = pAmount
        
    def setDate(self, d):
        self._policyDate = dat
        
    def __str__(self):
        string = "Policy Number: " + str(self._policyNumber)
        string += "\nPolicy Name: " + self._policyName
        string += "\nPolicy Address: " + self._policyAddress
        string += "\nPolicy Premium: " + str(self._policyPremium)
        return string

if __name__ == "__main__":
    sPolicy = Policy ("23187", "03-04-2019", "John Jones", "3 River St. N.Y., N.Y", 100)
    print(sPolicy)
    sPolicy._setNum("3333")
    sPolicy._setDate("12-25-2018")
    sPolicy._setAdd("5 Highway 1")
    sPolicy.setNam("Joe Thomas")
    sPolicy._setAmount (99)
    print(sPolicy.getNum(), sPolicy.getDate(), sPolicy.getAdd sPolicy.getAmount())
