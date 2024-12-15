from customer import Customer
from restaurant import Restaurant

sakib = Customer("sakib", "sakib@gmail.com", "ctg")
rakib = Customer("rakib", "rakib@gmail.com", "Dhaka")
akib = Customer("akib", "akib@gmail.com", "Cumilla")
rest = Restaurant()
rest.add_customer(sakib)
rest.add_customer(rakib)
rest.add_customer(akib)

rest.show_customers()