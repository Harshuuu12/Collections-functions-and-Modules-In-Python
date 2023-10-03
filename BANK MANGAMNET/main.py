from banker import Banker
from customer import Customer

def display():
    print("Bank Management System Menu:")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Exit")

def add_customer():
    name = input("Enter Customer Name: ")
    balance = float(input("Enter Initial Account Balance: "))
    customer = Customer(name, balance)
    banker.add_customer(customer)
    print("Customer Added Successfully")

def view_customers():
    print("All Customers:")
    banker.view_customers()

def main():
    while True:
        display()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_customer()
        elif choice == '2':
            view_customers()
        elif choice == '3':
            print("Exiting the program ")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
