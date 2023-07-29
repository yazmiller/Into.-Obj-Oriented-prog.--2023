class BankAccount: # save this code in BankAccount.py
    def __init__(self,n="",num = "",bal=0.0):
        self._acctName = n
        self._acctNumber = num
        self._acctBalance = bal
    def setAccountName(self,bname):
        self._acctName = bname
    def setAccountNumber(self,rn):
        self._acctNumber = rn
    def setAccountBalance(self,b):
        self._acctBalance = b
    def getAccountName(self):
        return self._acctName
    def getAccountNumber(self):
        return self._acctNumber
    def getAccountBalance(self):
        return self._acctBalance
    def __str__(self):
        return self._acctName + "\n" + (self._acctBalance)

if __name__ == "__main__":
    myAccount = BankAccount("judy", "1111", 3245.56)
    print(myAccount)
