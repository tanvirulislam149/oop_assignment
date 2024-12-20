class Restaurant:
    def __init__(self):
        self.menu = []  # [{item_name, price}, {}]
        self.customers = [] # [obj, obj]

    def add_item(self, item_name, price):
        item = {"item_name": item_name, "price": price}
        self.menu.append(item)
        print("Item added")

    def remove_item(self, item_name):
        flag = False
        for item in self.menu:
            if item["item_name"].lower() == item_name.lower():
                self.menu.remove(item)
                flag = True
        if flag:
            print("Item removed")
        else:
            print("Item not found")

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} Added")

    def remove_customer(self, customer_name):
        flag = False
        for c in self.customers:
            if c.name == customer_name:
                self.customers.remove(c)
                flag = True
                break
        if flag:
            print("Customer removed")
        else:
            print("Customer not found")

    def show_customers(self):
        print("-----------Customers List--------------")
        for customer in self.customers:
            print(f"Name: {customer.name}, Email: {customer.email}")

    def show_menu(self):
        print("-----------Restaurant Menu--------------")
        for item in self.menu:
            print(f"Name: {item["item_name"]}, Price: {item["price"]}")

    def customer_details(self, customer_name):
        flag = False
        customer = None
        for c in self.customers:
            if c.name == customer_name:
                flag = True
                customer = c
                break

        if flag:
            print(f"-----------{customer.name}'s Details--------------")
            print("Name: ", customer.name)
            print("Email: ", customer.email)
            print("Address: ", customer.address)
            for o in customer.orders:
                print(f"Item Name: {o['item_name']}, Total price: {o["total_price"]}, Quantity: {o['quantity']}")
            print("Balance: ", customer.balance)
        else:
            print("Customer not found")