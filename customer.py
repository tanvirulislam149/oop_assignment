class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.__orders = []
        self.__balance = 0
