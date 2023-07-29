from Policy import Policy

class LifePolicy(Policy):
    
    def __init__(self, age, smoker, medical_status):
        Policy().__init__(self, age, smoker, MedicalStatus)
        self._Age = age
        self._Smoker = smoker
        self._MedicalStatus = MedicalStatus
        
    def setAge(self,sage):
    		self._Age = sage
    def getAge(self):
        return sage 
    def setSmoker(self, ssmoker):
        self._smoker = ssmoker
    def getSmoker(self):
        return self._Smoker
    def setMedicalStatus(self, sMedicalStatus):
        self._MedicalStatus = sMedicalStatus  
    def getMedicalStatus(self):
        return self._MedicalStatus
  
    def __str__(self):
    			return Policy().__str__() + f"\nAge: {self._Age}\nSmoker: {self._Smoker}\nMedical Status: {self._MedicalStatus}"
          
     def Calculate_Premium(self):
        Premium = Policy().getPremium() + 100  
        if self._Smoker == "True":
            Premium += 25    
        if self._Age > 65:
            Premium += 100  
        if self._MedicalStatus in range(4,7):
            Premium += 50
        elif self._MedicalStatus in range(7,11):
            Premium += 100  
        Policy().setPremium(Premium)
