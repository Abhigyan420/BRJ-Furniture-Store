
from read import read_furniture_process
from write import write_furniture_process, generate_invoice_process

# Order furniture from manufacturer
def order_furniture_process(id_, quantity, employee_name):
    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    furniture_data = read_furniture_process()
    
    if id_ in furniture_data:
        furniture_data[id_]['quantity'] += quantity
        amount = furniture_data[id_]['price'] * quantity
        
        generate_invoice_process(
            'Order',
            id=id_,
            manufacturer=furniture_data[id_]['manufacturer'],
            product_name=furniture_data[id_]['product_name'],
            quantity=quantity,
            employee=employee_name,
            amount=amount
        )
        
        write_furniture_process(furniture_data)
        print(f"Order processed successfully. {quantity} units of furniture ID {id_} ordered.")
    else:
        print(f"Error: Furniture ID {id_} not found.")

# Sell furniture to customers
def sell_furniture_process(id_, quantity, customer_name, shipping_cost):
    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    if shipping_cost < 0:
        print("Shipping cost cannot be negative.")
        return

    furniture_data = read_furniture_process()
    
    if id_ in furniture_data:
        if furniture_data[id_]['quantity'] >= quantity:
            total_amount = furniture_data[id_]['price'] * quantity
            total_amount_with_shipping = total_amount + shipping_cost

            furniture_data[id_]['quantity'] -= quantity
            
            generate_invoice_process(
                'Sale',
                id=id_,
                manufacturer=furniture_data[id_]['manufacturer'],
                product_name=furniture_data[id_]['product_name'],
                quantity=quantity,
                customer_name=customer_name,
                price=furniture_data[id_]['price'],
                total_amount=total_amount,
                shipping_cost=shipping_cost,
                total_amount_with_shipping=total_amount_with_shipping
            )
            
            write_furniture_process(furniture_data)
            print(f"Sale processed successfully. {quantity} units of furniture ID {id_} sold to {customer_name}.")
        else:
            print(f"Error: Insufficient stock. Only {furniture_data[id_]['quantity']} units available.")
    else:
        print(f"Error: Furniture ID {id_} not found.")
