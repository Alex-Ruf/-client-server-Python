import json


def write_order_to_json(item, quantity, price, buyer, date):
    data = {
        'Item': item,
        "Quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date

    }
    with open('orders.json') as f:
        write_data =json.load(f)
        write_data['orders'].append(data)

    with open('orders.json', 'w') as f:
        f.write(json.dumps(write_data, indent=4))




write_order_to_json('PC', '15', '100', 'zero1', '22-2-2021')
write_order_to_json('tablet', '3', '4560', 'zenit', '10-2-2001')
