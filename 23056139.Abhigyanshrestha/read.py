
FURNITURE_FILE = 'furniture.txt'

# read the furniture data 
def read_furniture_process():
    
    with open(FURNITURE_FILE, 'r') as file:
        furniture_data = {}
        for line in file:
            parts = line.strip().split(', ')
            if len(parts) == 5:
                id_ = int(parts[0])
                manufacturer = parts[1]
                product_name = parts[2]
                quantity = int(parts[3])
                price = float(parts[4].replace('$', ''))
                furniture_data[id_] = {
                    'manufacturer': manufacturer,
                    'product_name': product_name,
                    'quantity': quantity,
                    'price': price
                }
    return furniture_data
