class Restaurant:
    def __init__(self):
        self.menu = []  # [{item_name, price}, {}]
        self.customers = [] # 

    def add_item(self, item_name, price):
        item = {"item_name": item_name, "price": price}
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


    def show_menu(self):
        print("-----------Restaurant Menu--------------")
        for item in self.menu:
            print(f"Name: {item["item_name"]}, Price: {item["price"]}")
        return ""

res = Restaurant()
res.add_item("pizza", 23)
res.add_item("burger", 33)
res.add_item("pasta", 43)
res.show_menu()
res.remove_item("PizzA")
res.show_menu()