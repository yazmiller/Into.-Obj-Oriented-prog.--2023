from CompanySales import CompanySales

def main():
    filename = "CompanySalesData.csv"
    Company = CompanySales("ABC","3 River St. N.Y.,N.Y.", filename)
    while True:
        print("Choose a category:")
        print("Belts: ")
        print("Shoes: ")
        print("Shirts: ")
        print("Done")

        choice = input("Enter your choice: ")
        if choice == "1":
            category = "Belts"
        elif choice == "2":
            category = "Shoes"
        elif choice == "3":
            category = "Shirts"
        elif choice == "4":
            break
        else:
            print("Invalid choice")
            continue
        data = company.filterData(category)
        company.stats(data)
        print("Company Name:", Company.getCompanyName())
	print("Company Address:", Company.getCompanyAddress())
 	print("Sales Data:")
	print(Company.getData())
	company2 = CompanySales("Best Stuff Around", "25 North First", filename)
 	data = company2.filterData("Shoes")
 	print("Company Address:", company2.getCompanyAddress(), "Company Name:", company2.getCompanyName())
    	print("Average:", company2.getAverage(data))
    	print("Min:", company2.getMin(data))
 	print("Max:", company2.getMax(data))

if __name__ == "__main__":
    main()
