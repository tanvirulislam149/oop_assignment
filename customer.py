from restaurant import Restaurant

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.__orders = []
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def orders(self):
        return self.__orders 

    def show_menu(self, restaurant):
        restaurant.show_menu()

    def place_order(self, restaurant, item_name, quantity):
        flag = False
        item = None
        for i in restaurant.menu:
            if i["item_name"].lower() == item_name.lower():
                flag = True
                item = i
                break
        if flag:
            total = item["price"] * quantity
            if total < self.balance:
                order = {"item_name": item_name, "total_price": total, "quantity": quantity}
                self.orders.append(order)
                self.balance = self.balance - total
                print("Order placed successfully")
            else:
                print("Not enough balance")
        else:
            print("Item not found")

res = Restaurant()
res.menu = [{"item_name": "pizza", "price": 34}, {"item_name": "burger", "price": 334}, {"item_name": "alu", "price": 4}]

s = Customer("s", "sasdf", "ctg")
s.place_order(res, "Pizza", 10)
s.place_order(res, "alu", 100)

print(s.orders)
print(s.balance)