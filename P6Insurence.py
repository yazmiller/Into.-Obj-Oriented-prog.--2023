from AutomobilePolicy import AutomobilePolicy
from LifePolicy import LifePolicy
from Policy import Policy

Policies = []
Life = LifePolicy("32115","10-20-20018","Jane Doe","3422 Howard Ave. Dallas
Mo",200,65,"True",5)
                  
Auto = AutomobilePolicy("32145","10-22-20018","Thomas Smith","3422 Main Columbia
Mo",100,2,1,"High")
                        
Policies.append(Life)
Policies.append(Auto)
                        
for i in range(len(Policies)):
    Policies[i].Calculate_Premium()
    print (Policies[i])
