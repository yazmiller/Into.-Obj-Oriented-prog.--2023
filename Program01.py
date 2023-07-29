#Yazmin Miller
#1/26/2023
#When I eneter a letter instead of a number at the prompt it gives me a error saying invalid literal for int() with base 10. So it means if int() it there I will need to put number. 
population = int(input("Enter the current popualtion: "))
birth = int(input("Enter the number of births from the previous year: "))
death = int(input("Enter the number of deaths from the previous year: "))
year = int(input("How many years you want to predit to? "))

birthrate = (birth/population) * 1000
print("The birth rate is ", birthrate)

deathrate = (death/population) * 1000
print("The death is ", deathrate)

growthrate = (birthrate - deathrate) / 10
print("The growth rate of the population is ", growthrate)

futurepopulation = int(population * pow((1 + growthrate / 100), year))
print("The predicted population would be", futurepopulation)

