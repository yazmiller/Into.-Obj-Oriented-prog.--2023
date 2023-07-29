#Yazmin Miller
#Date: 04/2/2023

def agi(waged, interest, unempoly):
    earn = float(wages + interest + unempoly)
    return earn

def status(mon):
    if mon == 0:
        return 6000
    elif mon == 1:
        return 12000
    elif mon == 2:
        return 24000
    else:
        print("ERROR: This cannot be deductions")

def taxable (ada, ded):
    total = ada - ded
    if total < 0:
        return 0
    else:
        return total

def own(sta, inc, gai):
    if sta == 0 or 1 and inc >=0 and inc <= 10000:
        return .1 * inc
    elif sta == 0 or 1 and inc >= 10001 and inc <= 40000:
        return 1000 + (.12 * gai) - 10000
    elif sta == 0 or 1 and inc >= 40001 and inc <= 85000:
        return 4600 + (.22 * gai) - 40000
    elif sta == 0 or 1 and inc >= 85000:
        return 14500 + (.24 * gai) - 85000
    elif sta == 2 and inc >= 0 and inc <= 20000:
        return .10 * inc
    elif sta == 2 and inc >= 20001 and inc <= 80000:
        return 2000 + (.12 * gai) - 20000
    elif sta == 2 and inc >= 80000:
        return 9200 + (.22 * gai) - 80000
    
   
if __name__ == "__main__":
    wages = float(input("Wages Earned: "))
    interest = float(input("Interest Earned: "))
    unemployment = float(input("Unemployment compensation: "))
    stat= float(input("Status: "))
    tax = float(input("Pre-paid taxes (taxes already paid): "))

    agi2 = agi(wages, interest, unemployment)
    print("AGI: ", agi2)
    status2 = status(stat)
    print("Deductions: ", status2)
    taxable2 = taxable(agi2, status2)
    print("Taxable amount of income: ", taxable2)
    own2 = own(stat, wages, interest)
    print("Taxes owned: ", own2)



