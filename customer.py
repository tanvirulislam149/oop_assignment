class Customer:
    def __init__(self, name, email, address):
        self.id = 0
        self.name = name
        self.email = email
        self.address = address
        self.__orders = []
        self.__balance = 0
