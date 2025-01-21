import json
car = """{"model": "Civic", "make": "Honda", "variants": ["Sedan", "Coupe"]}"""
print(car)
car_dict = json.loads(car) # load json and convert it into a Python dictionary
print(type(car))
print(car_dict)
print(type(car_dict))
print(car_dict['variants'])

with open("currency.json") as json_file:
    data = json.load(json_file)
    print(data)

currency = {"Country": "India", "Currency": "Rupee"}
json_var = json.dumps(currency) # converts the json dictionary into a string
print(json_var)
print(type(json_var))

written_data = json.load(open("currency.json"))
print(written_data)
print(type(written_data))

dessert = {"Name": "Ice cream", "Flavours": ["Chocolate", "Pineapple"], "Toppings": True, "WaffleCone": "Yes"}
dessert_str = json.dumps(dessert)
print(dessert_str)
print(type(dessert_str))

with open("eat.txt", "w") as json_file:
    json.dump(dessert_str, json_file)

json.dumps(dessert, indent=2)
print(json.dumps(dessert, separators=(":", "=")))
