import csv

"""
:var csvfile                    : This is the variable which we are opening csv file in that variable.
:var customer_orders            : This is the variable in which we are storing the csv file in the form of Read mode using 
                                  DictReader() method.
:var orders(Empty Dictionary)   : This is the empty dictionary variable name.
for loop                        : This is the for loop which we are fetching rows one by one from customer_orders.
if statement                    : This is the if statement which we are checking the order_number is present or not in the
                                  orders i.e. in empty dictionary in first iteration of the loop if present then condition 
                                  will be true and it will execute if part and will add the non repeated data i.e. product 
                                  data into the product list which is available in the dictionary otherwise if is is false 
                                  it will executes else part.
"""


csvfile = open('6.python_example.csv')

customer_orders = csv.DictReader(csvfile)
orders = {}

for row in customer_orders:
    if row['Order No'] in orders.keys():
        orders[row['Order No']]['Products'].append({'sku': row['SKU'], 'price': row['Price'], 'qty': row['Qty']})
    else:
        orders[row['Order No']] = {'customer': {'name': row['Customer'],
                                              'address 1 ': row['Address1'],
                                              'address 2': row['Address2'],
                                              'city': row['City'],
                                              'country': row['Country']},
                                 'Products': [{'sku': row['SKU'], 'price': row['Price'], 'qty': row['Qty']},]}
print(orders)

csvfile.close()