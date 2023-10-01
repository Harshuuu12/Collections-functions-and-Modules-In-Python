class Banker:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def view_customers(self):
        for customer in self.customers:
            print(customer)
