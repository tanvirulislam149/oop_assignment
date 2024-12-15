class Restaurant:
    def __init__(self):
        self.menu = []  # [{id, item_name, price}, {}]
        self.customers = [] # [{id, name, email, address...}]

    def add_item(self, item_name, price):
        item = {"id": len(self.menu) + 1,"item_name": item_name, "price": price}
        self.menu.append(item)

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
        customer.id = len(self.customers) + 1
        self.customers.append(customer)

    def show_customers(self):
        print("-----------Customers List--------------")
        for customer in self.customers:
            print(f"Id: {customer.id}, Name: {customer.name}, Email: {customer.email}")
        return ""        

    def show_menu(self):
        print("-----------Restaurant Menu--------------")
        for item in self.menu:
            print(f"Id: {item["id"]}, Name: {item["item_name"]}, Price: {item["price"]}")
        return ""

res = Restaurant()
res.add_item("pizza", 23)
res.add_item("burger", 33)
res.add_item("pasta", 43)
res.show_menu()
res.remove_item("PizzA")
res.show_menu()