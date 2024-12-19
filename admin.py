from restaurant import Restaurant
from main import restaurant

class Admin:
    def __init__(self, name):
        self.name = name

    def add_item(self, item_name, price):
        restaurant.add_item(item_name, price)

    def remove_item(self, item_name):
        restaurant.remove_item(item_name)

    def add_customer(self, customer):
        restaurant.add_customer(customer)

    def remove_customer(self, customer_name):
        restaurant.remove_customer(customer_name)

    def show_customers(self):
        restaurant.show_customers()

    def show_menu(self):
        restaurant.show_menu()

    def update_price(self, item_name, price):
        flag = False
        for item in restaurant.menu:
            if item["item_name"] == item_name:
                item["price"] = price
                flag = True
                break
        if flag:
            print("Price updated")
        else:
            print("Item not found")

    