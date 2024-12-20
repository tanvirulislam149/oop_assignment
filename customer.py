# file name --> customer.py

from restaurant import Restaurant

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.__orders = [] # array of dictionary
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

    def check_balance(self):
        print(f"Your balance is {self.balance}")

    def add_balance(self, value):
        self.balance = self.balance + value
        print(f"Your current balance is {self.balance}")

    def view_orders(self):
        for o in self.orders:
            print(f"Item name: {o['item_name']}, Total price: {o["total_price"]}, Quantity: {o["quantity"]}")