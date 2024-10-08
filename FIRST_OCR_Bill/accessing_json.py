import json

with open('output.json', 'r') as f:
    data = json.load(f)

# print(data['receipts'][0].keys())

print(data['receipts'][0]['merchant_name'])

print(data['receipts'][0]['merchant_address'])

print(data['receipts'][0]['merchant_phone'])

# print(data['receipts'][0]['merchant_website'])

# print(data['receipts'][0]['items'])
print(data['receipts'][0]['total'])

print(data['receipts'][0]['subtotal'])
print(data['receipts'][0]['tax'])