from datetime import date

class sales_transaction:
    def __init__(self):
        """==========================FOR PRODUCT=========================="""
        self.prd = 0
        self.products = {}
        self.product_stock = {}
        """==========================FOR CUSTOMER=========================="""
        self.cust = 0
        self.customer_details = {}
        self.customer_address = {}
        """==========================FOR SALE PRODUCT======================"""
        self.sale_order_no = 0
        self.sale_order_record = {}
        """==========================FOR DELIVERY ORDER======================"""
        self.DO = 0
        self.delivery_order = {}

    """=======METHODS FOR MANAGING THE CUSTOMER,PRODUCT AND ORDERS======="""

    def manage_customer(self):
        """
        :var cust_values: This is the variable which is used in the manage_customer(self) method for storing the return
        values from the prepare_customer(self) method in that variable.

        :var cust_key: This is the variable which is which is used in manage_customer(self) method for storing the key
        values.
        """
        cust_values = self.prepare_customer()
        cust_key = self.create_customer(cust_values)
        print(cust_key)

    def manage_product(self):
        """
        :var values: This is the variable which is used in the manage_product(self) method for storing the return
        values from the prepare_product(self) method in that variable.

        :var key: This is the variable which is which is used in manage_product(self) method for storing the key values.
        """

        values = self.prepare_product()
        key = self.create_product(values)
        print(key)

    def manage_orders(self):
        """
        :var values: This is the variable which is used in the manage_order(self) method for storing the return
        values from the prepare_sale_order(self) method in that variable.

        :var key: This is the variable which is which is used in manage_orders(self) method for storing the key values.
        """

        values = self.prepare_sale_order()

        # key = self.create_order(values)
        # print(key)

    """=================END OF MANAGING ALL THOSE THINGS================="""

    """=======METHODS FOR PREPARING THE CUSTOMER,PRODUCT AND ORDERS======="""

    def prepare_customer(self):

        """
        :return: This is the return statement from prepare_customer(self) method which is used for the returning the
        values like customer_name,customer_email,customer_phone,address1,address2,city,state,zipcode and country.

        :var [customer_name,customer_email,customer_phone,address1,address2,city,state,zipcode and country]: these are
        the variables which are used to accept the user input for returning the desire values in prepare_customer(self)
        method.

        """

        customer_name = input("Enter the customer name:=")
        customer_email = input("Enter the customer email id:=")
        customer_phone = input("Enter the customer phone:=")
        address1 = input("Enter the address1:=")
        address2 = input("Enter the address2:=")
        city = input("Enter the city:=")
        state = input("Enter the state:=")
        zipcode = input("Enter the zipcode:=")
        country = input("Enter the country:=")

        return {
            "customer_name": customer_name,
            "customer_email": customer_email,
            "customer_phone": customer_phone,
            "Address1": address1,
            "Address2": address2,
            "City": city,
            "State": state,
            "Zipcode": zipcode,
            "Country": country
        }

    def prepare_product(self):

        """
        :return: This is the return statement which is used for returning the values like product_name,product_unit_price,
        product_cost,stocks and product_types.

        :var product_name: This is the variable which is used for getting the user name through user input.

        :var product_unit_price: This is the variable which is used for getting the product price through the user input.

        :var product_cost: This is the variable which is used for getting the product stocks through the user input.

        :var choice: This is the variable which is used for select the choice through the user input.

        """
        global product_types
        product_name = input("Enter the product name:=")
        product_unit_price = int(input("Enter the product unit price:="))
        product_cost = int(input("Enter the product cost:="))
        stocks = int(input("Enter the stock:="))

        print("1.Stockable")
        print("2.Consumable")
        print("3.Service")

        choice = int(input("Enter the product type option:="))

        if choice == 1:
            product_types = 'Stockable'
        elif choice == 2:
            product_types = 'Consumable'
        elif choice == 3:
            product_types = 'Service'
        else:
            print("Wrong Product types...")

        return {
            "product_name": product_name,
            "product_unit_price": product_unit_price,
            "product_cost": product_cost,
            "Stocks": stocks,
            "product_types": product_types
        }

    def prepare_sale_order(self):
        oredrline = {}
        # print(self.customer_details)
        print("=======CREATE CUSTOMER=======")
        print(f"{'Customer ID':<15}  {'Customer Name':<15}")
        print("==============================")
        for k, v in self.customer_details.items():
            print(f"{k:<15}  {v.get('customer_name'):<15}")
        print("==============================")
        self.customer = input("Choose the customer:=")
        if self.customer in self.customer_details.keys():
            while True:
                print("1: Add Products")
                print("2: Exit")
                chose = int(input("Enter your choice:="))
                if chose == 1:
                    """============================ABOUT PRODUCT======================"""
                    # print(self.customer_details)
                    print("=====PREPARE SALE PRODUCT=====")
                    print(f"{'Product ID':<15}  {'Product Name':<15}")
                    print("==============================")
                    for k, v in self.product_stock.items():
                        print(f"{k:<15}  {v.get('product_name'):<15}")
                    print("==============================")
                    self.product = input("Choose the Product:=")

                    if self.product in self.product_stock.keys():
                        quantity = int(input("Enter The Produce Quantity:="))
                        if self.product in oredrline.keys():
                            oredrline.get(self.product)['quantity'] += quantity
                            oredrline.get(self.product)['subtotal'] = oredrline.get(self.product).get(
                                'quantity') * self.product_stock.get(self.product).get('product_unit_price')
                        else:
                            oredrline[self.product] = {'product_sku': self.product,
                                                       'unit_price': self.product_stock.get(self.product).get(
                                                           'product_unit_price'),
                                                       'quantity': quantity,
                                                       'subtotal': self.product_stock.get(self.product).get(
                                                           'product_unit_price') * quantity,
                                                       'state': 'draft'}
                    print("===========PRODUCTS===========")
                    print(f"{'Product SKU':<15}  {'Product Quantity':<15}")
                    print("==============================")
                    for k, v in self.products.items():
                        print(f"{k:<15}  {v:<15} ")
                    print("==============================")

                    print("Product", self.products)
                    print("Stocks", self.product_stock)

                    self.sale_order_no += 1
                    so_key = "so" + str(self.sale_order_no)

                    self.sale_order_record[so_key] = {'customer': self.customer,
                                                      'order_lines': [{'product_sku': self.product,
                                                                       'unit_price': self.product_stock.get(
                                                                           self.product).get(
                                                                           'product_unit_price'),
                                                                       'quantity': quantity,
                                                                       'subtotal': quantity * self.product_stock.get(
                                                                           self.product).get(
                                                                           'product_unit_price'),
                                                                       'state': 'Draft'}]}

                    print("This is sale order record....", self.sale_order_record)

                    print("This is Order Line:=", oredrline)
                elif chose == 2:
                    break
                else:
                    print("This is wrong choice...")

    """=================END OF PREPARING ALL THOSE THINGS================="""

    """=======METHODS FOR CREATING THE CUSTOMER AND PRODUCT======="""

    def create_customer(self, cust_values):
        self.cust += 1
        address1 = cust_values.pop("Address1")
        address2 = cust_values.pop("Address2")
        city = cust_values.pop("City")
        state = cust_values.pop("State")
        zipcode = cust_values.pop("Zipcode")
        country = cust_values.pop("Country")
        cust_key = "cust" + str(self.cust)
        self.customer_details.update({cust_key: cust_values})
        self.customer_address.update({cust_key: {"Address1": address1, "Address2": address2, "City": city,
                                                 "State": state, "Zipcode": zipcode, "Country": country}})

        print("========CREATE CUSTOMER=======")
        print(f"{'Customer ID':<15}  {'Customer Name':<15}")
        print("==============================")
        for k, v in self.customer_details.items():
            print(f"{k:<15}  {v.get('customer_name'):<15}")
        print("==============================")

        print("Customer Address:=", self.customer_address)
        print("Customer Details:=", self.customer_details)
        return cust_key

    def create_product(self, values):
        """
        :param values:= This is parameter from create_product method in this parameter contains the return values
        of the create product and this return value is used for creating the new dictionary with pop operation for
         this method i.e. for create_product(self,values) method.

        :var var:= This is the variable which is used for soring the popped values from values variable/parameter.

        :var key:= This is the variable which is used for storing the newly generated PRD-values in this variable.

        """
        self.prd += 1
        var = values.pop("Stocks")
        key = "prd" + str(self.prd)
        self.product_stock.update({key: values})
        self.products.update({key: var})

        print("========CREATE PRODUCT========")
        print(f"{'Product ID':<15}  {'Product Name':<15}")
        print("==============================")
        for k, v in self.product_stock.items():
            print(f"{k:<15}  {v.get('product_name'):<15}")
        print("==============================")

        print(self.products)
        print(self.product_stock)

    """=================END OF CREATION OF ALL THOSE THINGS================="""

    def increase_stocks(self):
        print("1.Increase product")
        print("2.Exit")
        print(self.product_stock)

        choice = int(input("Enter the choice:="))

        if choice == 1:
            prd = input("Enter the PRD values:=")
            if prd in self.products.keys():
                stock_value = int(input("How much stock you want to add:="))
                self.products[prd] += stock_value
            else:
                print("Wrong output please try again...")
            print(self.products)

    def sale_product(self):
        print("1.List of the products")
        print("2.Exit")

        choice = int(input("Enter the choice:="))

        if choice == 1:
            print(self.product_stock)
        else:
            print("Wrong")
    """==========================STATE SECTION==============================="""
    def change_state(self):
        print("List of the sale_orders:=")
        for k in self.sale_order_record.keys():
            print(k)
        self.choice_sale_order = input("Enter the sale order code:=")

        while True:
            print("1.Draft")
            print("2.Conform")
            print("3.Done")
            print("4.Cancel")
            print("5.Exit")

            choice = int(input("Enter the state option:="))

            if choice == 1:
                self.draft_state()
            elif choice == 2:
                self.conform_state()
            elif choice == 3:
                self.done_state()
            elif choice == 4:
                self.cancel_state()
            elif choice == 5:
                break
            else:
                print("Wrong")

    def draft_state(self):
        for var_draft in self.sale_order_record[self.choice_sale_order]['order_lines']:
            if var_draft['state'] == 'Draft':
                print("Already in Draft")
            elif var_draft['state'] == 'Cancel':
                var_draft['state'] = 'Draft'
                self.sale_order_record[self.choice_sale_order]['state'] = 'Draft'
                print(self.sale_order_record)
            elif var_draft['state'] == 'Conform':
                var_draft['state'] = 'Draft'

                print(self.sale_order_record)
            elif var_draft['state'] == 'Done':
                print("Already Done")
                print(self.sale_order_record)

    def conform_state(self):
        for var_conform in self.sale_order_record[self.choice_sale_order]['order_lines']:
            if var_conform['state'] == 'Conform':
                print("Already Conform")
            elif var_conform['state'] == 'Cancel':
                print("Not possible")
                print(self.sale_order_record)
            elif var_conform['state'] == 'Draft':
                var_conform['state'] = 'Conform'
                self.manage_delivery_order(self.choice_sale_order)
                print(self.sale_order_record)
            elif var_conform['state'] == 'Done':
                print("Already Done")
                print(self.sale_order_record)

    def done_state(self):
        for var_done in self.sale_order_record[self.choice_sale_order]['order_lines']:
            if var_done['state'] == 'Done':
                print("Already Done")
            elif var_done['state'] == 'Conform':
                var_done['state'] = 'Done'
                sale_order_dict = self.sale_order_record[self.choice_sale_order].get('order_lines')[0].get('quantity')
                product_dict = self.products[self.product]
                updated_quantity = product_dict - sale_order_dict
                self.products[self.product] = updated_quantity

                print(sale_order_dict, product_dict)
                print(self.products)
            elif var_done['state'] == 'Draft':
                var_done['state'] = 'Done'

                sale_order_dict = self.sale_order_record[self.choice_sale_order].get('order_lines')[0].get('quantity')
                product_dict = self.products[self.product]
                updated_quantity = product_dict - sale_order_dict
                self.products[self.product] = updated_quantity

                print(self.sale_order_record)
            elif var_done['state'] == 'Cancel':
                print("Not possible to Done state")
                print(self.sale_order_record)

    def cancel_state(self):
        for var_cancel in self.sale_order_record[self.choice_sale_order]['order_lines']:
            if var_cancel['state'] == 'Done':
                print("Sorry Can't cancel...")
            elif var_cancel['state'] == 'Conform':
                sale_order_data = self.sale_order_record.get(self.choice_sale_order)
                print(sale_order_data)
                if sale_order_data.get('order_lines')[0]['state'] != 'Cancel':
                    print('First you need to canel this delivery order !')
                    self.cancel_delivery_order()
                else:
                    for data in sale_order_data.get('stock_moves'):
                        data['state'] = 'Cancel'
                    sale_order_data['state'] = 'Cancel'
                    var_cancel['state'] = 'Cancel'
                    self.sale_order_record[self.choice_sale_order]['state'] = 'Cancel'
                print(self.delivery_order)
                print(self.sale_order_record)
            elif var_cancel['state'] == 'Draft':
                var_cancel['state'] = 'Cancel'
                print(self.sale_order_record)
            elif var_cancel['state'] == 'Cancel':
                print("Already cancel")
                print(self.sale_order_record)

    """=======================END OF STATE SECTION============================"""

    def create_order(self, values):

        print(self.sale_order_record)
        self.cust_key = input("Enter the customer key:=")
        unit_price = int(input("Enter the unit price:="))

        if self.cust_key in self.customer_details.items():
            self.sale_order_record.update(self.customer_details)
            print(self.sale_order_record)

    def print_bill(self):
        print("Which bill do you want to print?????:=")
        for k in self.sale_order_record.keys():
            print(k)
        choice_sale_order = input("Enter the sale order code:=")

        print("====================FINAL BILL======================")
        if choice_sale_order in self.sale_order_record:
            print(f'Order No : {choice_sale_order}			    Order Date : {date.today()}')
            v = self.sale_order_record[choice_sale_order]['order_lines']
            for i in v:
                print(f"State : {i['state']}")
            print(
                f"Customer : {self.sale_order_record[choice_sale_order].get('customer')},{self.customer_details[self.customer].get('customer_name')}			    address 1 : {self.customer_address[self.customer].get('Address1')}")
            print(
                f" {self.customer_details[self.customer].get('customer_phone')}						{self.customer_address[self.customer].get('Address2')}")
            print(
                f" {self.customer_details[self.customer].get('customer_email')}						{self.customer_address[self.customer].get('City')}, {self.customer_address[self.customer].get('State')}")
            print(f"{self.customer_address[self.customer].get('Zipcode')}")

            print(f"Product Name  	Product Price 	 Product Quantity  	Subtotal ")
            print("=================================================================")
            print(f"{self.product_stock[self.product].get('product_name')}		"
                  f"	   {self.sale_order_record[self.choice_sale_order]['order_lines'][0].get('unit_price')}    "
                  f"            {self.sale_order_record[self.choice_sale_order]['order_lines'][0].get('quantity')}	 "
                  f"	        {self.sale_order_record[self.choice_sale_order]['order_lines'][0].get('subtotal')}   ")
            print("=================================================================")
        else:
            print("Wrong choice...please try again")
    """======================DELIVERY ORDER SECTION==========================="""

    def manage_delivery_order(self, sale_order_id):

        values = self.prepare_delivery_order(sale_order_id)
        key = self.create_delivery_order(values)
        print(key)

    def prepare_delivery_order(self, sale_order_id):
        if self.sale_order_record:
            if sale_order_id:
                order = self.sale_order_record.get(sale_order_id)
                order_lines_data = [
                    {'product_code': order_line['product_sku'], 'product_qty': order_line['quantity'], 'state': 'Draft'}
                    for order_line in order.get('order_lines')]
                return {'sales_order': sale_order_id, 'customer id': order.get('customer'),
                        'stock_moves': order_lines_data, 'state': 'Draft'}
            else:
                print("Empty ! ")
        else:
            print("There is no order !")

    def create_delivery_order(self,values):
        self.DO += 1
        do_key = "DO" + str(self.DO)
        self.delivery_order.update({do_key: values})
        return do_key

    def validate_delivery_order(self):
        # for key, value in self.delivery_order.items():
        #     print(f'{key} {value}')
        print(self.delivery_order)
        order_id = input("Enter the order ID:=")
        if order_id in self.delivery_order:
            order = self.delivery_order.get(order_id)
            for stock_moves in order.get('stock_moves'):
                stock_moves['state'] = 'Done'
            order['state'] = 'Done'

            sale_order_data = self.sale_order_record.get(order.get('sales_order'))
            print(sale_order_data)
            for order_line in sale_order_data.get('order_lines'):
                order_line['state'] = 'Done'
            sale_order_data['state'] = 'Done'

        print(self.delivery_order)
        print(self.sale_order_record)

    def cancel_delivery_order(self):
        print(self.delivery_order)
        order_id = input("Enter the order ID:=")
        if order_id in self.delivery_order:
            order = self.delivery_order.get(order_id)
            for stock_moves in order.get('stock_moves'):
                stock_moves['state'] = 'Cancel'
            order['state'] = 'Cancel'

            sale_order_data = self.sale_order_record.get(order.get('sales_order'))
            print(sale_order_data)
            for order_line in sale_order_data.get('order_lines'):
                order_line['state'] = 'Cancel'
            sale_order_data['state'] = 'Cancel'

        print(self.delivery_order)
        print(self.sale_order_record)

    """===================END OF DELIVERY ORDER SECTION========================"""

c1 = sales_transaction()

while True:
    print("1.Create product")
    print("2.Create customer")
    print("3.Increase stocks")
    print("4.Sale Order")
    print("5.Change state")
    print("6.Print Bill")
    print("7.Validate delivery order")
    print("8.Cancel delivery order")
    print("9.Exit")

    choice = int(input("Enter your choice:="))

    if choice == 1:
        c1.manage_product()
    elif choice == 2:
        c1.manage_customer()
    elif choice == 3:
        c1.increase_stocks()
    elif choice == 4:
        c1.manage_orders()
    elif choice == 5:
        c1.change_state()
    elif choice == 6:
        c1.print_bill()
    elif choice == 7:
        c1.validate_delivery_order()
    elif choice == 8:
        c1.cancel_delivery_order()
    elif choice == 9:
        break
    else:
        print("Please try again...")
