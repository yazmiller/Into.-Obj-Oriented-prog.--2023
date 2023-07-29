class salesItem:
    def __init__(self, des, dte,amt, upe, epe):
        self._accountNumber = des
        self._category = dte
        self._quanity = amt
        self._unitPrice = upe
        self._extendedPrice = epe
    def setaccountNumber(self,saccountNumber):
        self._accountNumber = saccountNumber
    def setcategory(self,scategory):
        self._category = scategory
    def setquanity(self,squanity):
        self._quanity = squanity
    def setunitPrice(self,sunitPrice):
        self._unitPrice = sunitPrice
    def setextendedPrice(self,sextendedPrice):
        self._extendedPrice = sextendedPrice

        
    def getaccountNumber(self):
        return self._accountNumber
    def getcategory(self):
        return self._category
    def getquanity(self):
        return self._quanity
    def getunitPrice(self):
        return self._unitPrice
    def getextendedPrice(self):
        return self._extendedPrice
    def __str__(self):
        return "\n" + str(self._accountNumber) + "\n" + str(self._category) + "\n" + str(self._quanity) + "\n"+ str(self._unitPrice) + "\n" + str(self._extendedPrice)

if __name__ == "__main__":
    anItem = salesItem("101010", "red", "100", "2", "2")
    print(anItem)
    anItem.setaccountNumber("101010")
    anItem.setcategory("red")
    anItem.setquanity("100")
    anItem.setunitPrice("2")
    anItem.setextendedPrice("2")
    print(anItem)
    print(anItem.getaccountNumber(), anItem.getcategory(), anItem.getquanity(), anItem.getunitPrice(), anItem.getextendedPrice())
