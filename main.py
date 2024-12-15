from customer import Customer
from restaurant import Restaurant


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
        if admin_name == "Admin":
            while True:
                print("-------Admin Menu-----------")
                print("1. Create Customer Account")
                print("2. Remove Customer Account")
                print("3. View all Customer")
                print("4. Manage Restaurant Menu")
                print("5. Exit")
                a = int(input("Select an option: "))
                if a == 1:
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    address = input("Enter address: ")
                    customer = Customer(name, email, address)
                    restaurant.add_customer(customer)
                elif a == 2:
                    id = int(input("Enter Customer id: "))
                    restaurant.remove_customer(id)
                elif a == 3:
                    restaurant.show_customers()
                elif a == 4:
                    pass
                elif a == 5:
                    break
    elif n == 2:
        pass
    elif n == 3:
        break