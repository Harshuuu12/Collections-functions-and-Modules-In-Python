from banker import Banker
from customer import Customer

banker = Banker()

def display_menu():
    print("Bank Management System Menu:")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Exit")

def add_customer():
    name = input("Enter customer name: ")
    balance = float(input("Enter initial account balance: "))
    customer = Customer(name, balance)
    banker.add_customer(customer)
    print("Customer added successfully!")

def view_customers():
    print("All Customers:")
    banker.view_customers()

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_customer()
        elif choice == '2':
            view_customers()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
