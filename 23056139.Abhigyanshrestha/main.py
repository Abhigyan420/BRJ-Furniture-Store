from operation import order_furniture_process, sell_furniture_process
from read import read_furniture_process

# Display the available furniture
def show_furniture_list():
    furniture_data = read_furniture_process()
    for id_, details in furniture_data.items():
        print(f"ID: {id_}, Manufacturer: {details['manufacturer']}, Product: {details['product_name']}, Quantity: {details['quantity']}, Price: ${details['price']}")

# Get integer input for validation
def validate_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number eg. 1")

# Get float input for validation
def validate_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number eg. 500.56")


def welcome():
    print("*************************************************************************************************************************************************")
    print("                                                            Welcome To BRJ Furniture Store")
    print("                                                            Thankot, Kathmandu | 9808190819")
    print("                                                 Embrace the art of living beautifully—your dream space awaits!")
    print("*************************************************************************************************************************************************")

welcome()


# Interact with the user
def main():
    while True:
        print()
        
        print("\nPlease select an option:")
        print()
        print("-> Press 1: *To display the available furniture*")
        print("-> Press 2: *To buy from the manufacturer*" )
        print("-> Press 3: *To sell furniture to customer*")
        print("-> Press 4: *To Exit from  the system*")
        print("*************************************************************************************************************************************************")
        print()
        choice = input("Enter your choice: ")

        if choice == '1':
            show_furniture_list()
        elif choice == '2':
            id_ = validate_int_input("Enter Furniture ID to order: ")
            quantity = validate_int_input("Enter quantity to order: ")
            employee_name = input("Enter your name (Employee name): ")
           
            order_furniture_process(id_, quantity, employee_name)
            print("Order process completed successfully!")
        elif choice == '3':
            id_ = validate_int_input("Enter Furniture ID to sell: ")
            quantity = validate_int_input("Enter quantity to sell: ")
            customer_name = input("Enter customer name: ")
            shipping_cost = validate_float_input("Enter shipping cost: $")
            sell_furniture_process(id_, quantity, customer_name, shipping_cost)
            print("Sell process completed successfully!")
        elif choice == '4':
            print("Exiting the program."  "\n" "Thank you for visiting BRJ Furniture Store!")
            break
        else:
            print("Invalid choice, please enter the number between 1 to 4.")

if __name__ == "__main__":
    main()
