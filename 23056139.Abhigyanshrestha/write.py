
FURNITURE_FILE = 'furniture.txt'
INVOICE_FILE = 'invoice.txt'

def write_furniture_process(furniture_data):
    with open(FURNITURE_FILE, 'w') as file:
        for id_, details in furniture_data.items():
            line = f"{id_}, {details['manufacturer']}, {details['product_name']}, {details['quantity']}, ${details['price']}\n"
            file.write(line)

# Generate an invoice and print the receipt
def generate_invoice_process(transaction_type, **kwargs):
    import datetime
    now = datetime.datetime.now()
    
    # Build the invoice text
    invoice_text = (
        f"\n{'-'*100}\n"
        "***BRJ FURNITURE STORE***\n"
        "  ---- -Thankot, Kathmandu-----\n"
        "-----------------------------------------------------------------\n"
        f"Date: {now.strftime('%Y-%m-%d')}\n"
        f"Transaction Type: {transaction_type}\n"
    )
    
    if transaction_type == 'Order':
        invoice_text += (
            "--------------------------------------------------------------\n"
            f"Employee: {kwargs.get('employee')}\n"
            f"ID: {kwargs.get('id')}\n"
            f"Manufacturer: {kwargs.get('manufacturer')}\n"
            f"Product: {kwargs.get('product_name')}\n"
            f"Quantity: {kwargs.get('quantity')}\n"
            "----------------------------------------------------------------\n"
            f"Amount to Pay: ${kwargs.get('amount'):.2f}\n"
            "----------------------------------------------------------------\n"
            
            "--------------------Thank You for choosing us. Please visit again.--------------------\n"
        )
    
    elif transaction_type == 'Sale':
        invoice_text += (
            "--------------------------------------------------------------\n"
            f"Customer: {kwargs.get('customer_name')}\n"
            f"ID: {kwargs.get('id')}\n"
            f"Manufacturer: {kwargs.get('manufacturer')}\n"
            f"Product: {kwargs.get('product_name')}\n"
            f"Quantity: {kwargs.get('quantity')}\n"
            f"Price per Unit: ${kwargs.get('price'):.2f}\n"
            f"Total Amount: ${kwargs.get('total_amount'):.2f}\n"
            f"Shipping Cost: ${kwargs.get('shipping_cost'):.2f}\n"
            "----------------------------------------------------------------\n"
            f"Total Amount to Pay: ${kwargs.get('total_amount_with_shipping'):.2f}\n"
            "----------------------------------------------------------------\n"
            "Goods once sold will not be returned.\n"
            "Exchange within 7 days with the receipt except Saturday.\n"
            "----------------------------------------------------------------\n"
            "--------------------Thank You for choosing us. Please visit again.--------------------\n"
        )

    # Write the invoice to the file
    with open(INVOICE_FILE, 'a') as file:
        file.write(invoice_text)

    # Print the invoice to the terminal
    print(invoice_text)
