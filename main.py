from customer import Customer
from restaurant import Restaurant
from admin import Admin


# res.add_item("pizza", 23)
# res.add_item("burger", 33)
# res.add_item("pasta", 43)
# res.show_menu()
# res.remove_item("PizzA")
# res.show_menu()


# sakib = Customer("sakib", "sakib@gmail.com", "ctg")
# rakib = Customer("rakib", "rakib@gmail.com", "Dhaka")
# akib = Customer("akib", "akib@gmail.com", "Cumilla")

# res.add_customer(sakib)
# res.add_customer(rakib)
# res.add_customer(akib)

# res.show_customers()
# res.remove_customer(2)
# res.show_customers()


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
                        print("4. Exit")
                        menu_op = int(input("Select an option: "))
                        if menu_op == 1:
                            name = input("Enter item name: ")
                            price = input("Enter price: ")
                            admin.add_item(restaurant, name, price)
                        elif menu_op == 2:
                            id = input("Enter item name: ")
                            admin.remove_item(restaurant, id)
                        elif menu_op == 3:
                            admin.show_menu(restaurant)
                        elif menu_op == 4:
                            break
                elif admin_op == 5:
                    break
        else:
            print("Wrong Admin name")
    elif n == 2:
        pass
    elif n == 3:
        print("Closing the system")
        break