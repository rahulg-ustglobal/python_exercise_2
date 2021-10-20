"""
Program - 4
● Write a program which is having a class InventoryManagement.
● System should manage the quantity of purchase and sales processes.
● Users should be able to purchase the product with different prices in the same object of Inventory Management
- Use a dictionary, maintain a numerical index and store product price and product quantity against it.
● Whenever the product is sold, it will start deducting the product qty whichever entry is done first in the dictionary,
so qty will be deducted as FIFO (First In First Out).
● Once the qty from each purchase is used make sure, it is not used again, so update the dictionary accordingly.
● Program should be able to handle the valuation.
● Formula for valuation - sum of price * qty / sum of total qty.
● Write appropriate constructor, methods to manage the sales and purchase processes.
● There should be a provision to view the available quantities.
● This should be a menu driven program, which allows to
    *Purchase Product
    *Sale Product
    *View Available Product Quantities
    *Exit
● Whenever sales take place, the system should process the quantities and then should show the available quantities.
"""
class InventoryManagement:
    def __init__(self):
        """
        InventoryManagement(class) : This is the class we have to create the class for three of the methods.
        dict(Global Dictionary)    : This is the dictionary I have created for globally and it is for performing some
                                     operations like for incrementing the count,fro adding the product quantity like that.
        """
        self.product_stock={}
        self.count = 1
    def purchase_product(self,price,quantity):
        """
        method (purchase_product) : This is first method which is available in the InventoryManagement class
                                    and this method is used for how to manage the product price and product quantity
                                    from the dictionary.
        :param (price)           : This is parameter 1 of the purchase_product method which is used for
                                    saving the value of the price which is having the price as a key of the dictionary.
        :param (quantity)        : This is parameter 2 of the purchase_product method which is used for saving the
                                    quantity of the product in the dictionary which is having key as quantity.
        """
        self.product_stock[self.count] = {"price": price,"quantity": quantity}
        self.count += 1
        print("====================================")
        print(f"{'Product ID':<15}{'Price':<10}{'Quantity':<10}")
        print("====================================")
        for k,v in self.product_stock.items():
            print(f"{k:<15}{v.get('price'):<10}{v.get('quantity'):<10}")
        print("====================================")

    def sale_product(self,quantity):
        """
                :param quantity      : This is variable of the sale_product method which is used for saving the quantity
                                       of the products.
                :var total           : This is the variable of the sale_product method which is used saving the total
                                       storing the total quantity of the products.
                :var (delkey) of list: This is the list which is created for storing the empty keys of the dictionary.

                for loop (1)         : This is the first for loop from the sale_product which is created for getting the
                                       total values of the quantity from the product_stock
                for loop (2)         : This is the second for loop from the sale_product which is created for deleting
                                       the empty dictionaries which is available count of that in the delkey list.
                if statement (1)     : This is first if statement from

                :return:
        """
        total = 0
        delkey = []
        for value in self.product_stock.values():
            total += value.get("quantity")
        if quantity > 0:
            if quantity > total:
                print("You have entered the quantity greater than total quantity of the products...Please try again")
            else:
                for key, value in self.product_stock.items():
                    if quantity >= value.get("quantity"):
                        quantity -= value.get("quantity")
                        value["quantity"] = 0
                        delkey.append(key)
                        print(key)
                    else:
                        value["quantity"] -= quantity
                        quantity -= quantity
        for x in delkey:
            del (self.product_stock[x])

    def view_available_product(self):
        """
        method (view_available_product) : This is method which is available in InventoryManagement class.
                                          This method is created only because of to display the available products
                                          from the dictionary.
        """
        print(self.product_stock)
c1 = InventoryManagement()

"""
   :var choice   : This is the variable which is available in the while loop, This variable is created to get the choice
                   from the user according to the given options.
   :var price    : This is the variable which is created for accepting the input from the user as the quantity price.
   :var quantity : This is the variable which is created for accepting the input from the user as the quantity of the product.
   
"""

while True:
    print("1.Purchase Product")
    print("2.Sale Product")
    print("3.View Available Product Quantities")
    print("4.Exit")

    choice = int(input("Enter your choice:="))

    if choice == 1:
        price = int(input("Enter the purchase product price:="))
        quantity = int(input("Enter the quantity:="))
        c1.purchase_product(price,quantity)
    elif choice == 2:
        quantity = int(input("Enter the sale product quantity:="))
        c1.sale_product(quantity)
    elif choice == 3:
        c1.view_available_product()
    elif choice == 4:
        break
    else:
        print("Please try again...")