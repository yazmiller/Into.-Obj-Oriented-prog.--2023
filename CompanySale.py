class CompanySales:
    def __init__(self, name, address, filename):
        self._Name = name
        self._address = address
        self._data = []
        with open(filename, 'r') as f:
            for line in f:
                data = line.strip().split(',')
                self._data.append(SalesItem(data[0], data[1], data[2], data[3]))

    def setCompanyName(self,cname):
        self._Name = cname
    def setCompanyAddress(self, caddress):
        self._address = caddress

    def getCompanyName(self):
        return self._Name

    def getCompanyAddress(self):
        return self._address

    def __str__(self):
        return f"Company Name: {self._Name}\nCompany Address: {self._address}"

    def filter_data(self, category):
        return [sale for sale in self._data if sale._category == category]

    def stats(self, sales_data):
        prices = [sale.extended_price for sale in sales_data]
        return f"Average cost: {sum(prices) / len(prices)}\nMinimum sales price: {min(prices)}\nMaximum sales price: {max(prices)}"


class SalesItem:
    def __init__(self, date, category, description, extended_price):
        self._date = date
        self._category = category
        self._description = description
        self._extended_price = float(extended_price)

if __name__ == '__main__':
    sales = CompanySales("ABC","3 River St. N.Y.,N.Y.", "CompanySalesData.csv")
    print(sales)
    sales.setCompanyName("Dallas Store")
    sales.setCompanyAdreess("2929 First St., Dallas,Tx.")
    print("Company Name was changed to")
    print(sales.getCompanyName())
    print("Company Address was changed to")
    print(sales.getCompanyAddress())            
    filtered_data = sales.filter_data("Category A")
    print(sales.stats(filtered_data))
