from customer import Customer
from restaurant import Restaurant
from admin import Admin 

restaurant = Restaurant()
while True:
    print("-------Restaurant System-----------")
    print("1. Admin Login")
    print("2. Customer Login")
    print("3. Exit")
    n = int(input("Select an option: "))
    if n == 1:
        admin_name = input("Enter Admin Name: ")
        admin = Admin(admin_name)
        if admin.name == "Admin":
            while True:
                print("-------Admin Menu-----------")
                print("1. Create Customer Account")
                print("2. Remove Customer Account")
                print("3. View all Customer")
                print("4. Manage Restaurant Menu")
                print("5. Exit")
                admin_op = int(input("Select an option: "))
                if admin_op == 1:
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    address = input("Enter address: ")
                    customer = Customer(name, email, address)
                    admin.add_customer(restaurant, customer)
                elif admin_op == 2:
                    customer_name = input("Enter Customer name: ")
                    admin.remove_customer(restaurant, customer_name)
                elif admin_op == 3:
                    admin.show_customers(restaurant)
                elif admin_op == 4:
                    while True:
                        print("------------Manage Menu-----------")
                        print("1. Add items in Menu")
                        print("2. Remove items in Menu")
                        print("3. Show all items")
                        print("4. Update price of an item")
                        print("5. Exit")
                        menu_op = int(input("Select an option: "))
                        if menu_op == 1:
                            name = input("Enter item name: ")
                            price = input("Enter price: ")
                            admin.add_item(restaurant, name, price)
                        elif menu_op == 2:
                            name = input("Enter item name: ")
                            admin.remove_item(restaurant, name)
                        elif menu_op == 3:
                            admin.show_menu(restaurant)
                        elif menu_op == 4:
                            item_name = input("Enter item name: ")
                            price = int(input("Enter price: "))
                            admin.update_price(restaurant, item_name, price)
                        elif menu_op == 5:
                            break
                elif admin_op == 5:
                    break
        else:
            print("Wrong Admin name")
    elif n == 2:
        name = input("Enter customer name: ")
        flag = False
        customer = None
        for c in restaurant.customers:
            if c.name == name:
                flag = True
                customer = c
                break
        if flag:
            print(f"Welcome {name}")
            while True:
                print(f"---------{name}'s Menu----------")
                print("1. View restaurant menu")
                print("2. Place an order")
                print("3. Check balance")
                print("4. Add balance")
                print("5. View your orders")
                print("6. Exit")
                customer_op = int(input("Enter option: "))
                if customer_op == 1:
                    customer.show_menu(restaurant)
                elif customer_op == 2:
                    name = input("Enter item name: ")
                    quantity = int(input("Enter quantity: "))
                    customer.place_order(restaurant, item_name, quantity)
                elif customer_op == 6:
                    break
        else:
            print("User not found")
    elif n == 3:
        print("Closing the system")
        break