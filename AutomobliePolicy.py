from Policy import Policy

class AutomobilePolicy(Policy):
    def __init__(self, tra, acc, age, , premium):
        Policy().__init__ (self, tra, acc, age, , premium):
        self._tickets = tra
        self._accidents = acc
        self._ageRisk = age
  
  	def setTraffic(self, sTraffic):
        self._Traffic = sTraffic
    def getTraffic(self):
        return self._Traffic
    def setAccidents(self, sAccidents):
    		self._Accidents = sAccidents
    def getAccidents(self):
        return self._Accidents
    def setageRisk(self, sageRisk):
    		self._age_risk = sageRisk
    def getageRisk(self):
        return self._ageRisk
    def __str__(self):
        return Policy().__str__() + f"\nNumber of Traffic Tickets: {self._Traffic}\nNumber of Accidents: {self._Accidents}\nAge Risk: {self._ageRisk}"
    
    def calculate_premium(self):
        if self._traffic <= 2:
            add_premium = 25
        elif self._traffic <= 4:
            add_premium = 50
        else:
            add_premium = 100
        
        if self._Accidents <= 1:
            acc_premium = 0
        elif self._Accidents <= 3:
            acc_premium = 50
        else:
            acc_premium = 100
        
        if self.age_risk == "Low":
            age_premium = 0
        elif self.age_risk == "Medium":
            age_premium = 40
        else:
            age_premium = 120
        
        self.premium += add_premium + acc_premium + age_premium
