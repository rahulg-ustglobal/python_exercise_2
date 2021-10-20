"""
Program - 1
● Write a program that contains a ‘manufacturing’ class which allows product
manufacturing.
● It purchases raw material from the market and produces a product.
● One should manage the raw material product to produce the actual product.
● One should manage the ratio of raw material to produce the actual product.
○ Example - 2 wheels(raw material) are required to produce 1
bicycle(actual product)
● Take input from user raw material, raw material ratio qty, actual product
● While producing the actual product, if the system doesn’t have enough of its
stock of raw material, it should show a warning message as “Not enough raw
material available to produce the product, please do the purchase”.
● Program should be menu driven allowing to
○ Purchase Raw Material Product
○ Manufacture Actual Product
○ Show Raw Material Quantity
○ Show Actual Product Quantity
○ Exit
Following attributes and method function should be part of the class
○ Appropriate constructor to set the values for raw material product,
actual product, raw material ratio qty value
○ produce() - taking no qty to be produced for actual product as
argument
○ display_raw_material_stock()
○ display_final_product_stock()
○ purchase_raw_material() - taking no of qty of raw material to be
purchased
"""

class manufacturing:
    def __init__(self, raw_qty, ratio, actual_product):
        print("This is constructor")
        self.ratio = ratio
        self.raw_qty = raw_qty
        self.actual_product = actual_product
        self.actual_product_qty = 0

    def purchase_raw_material(self):
        self.raw_qty += int(input("How much you want to purchase:="))

    def produce(self):
        product_qty = int(input("How many products you want to produce:="))
        if product_qty * int(self.ratio[1]) > self.raw_qty:
            print("Not enough raw material")
        else:
            self.actual_product_qty += product_qty
            self.raw_qty -= product_qty * int(self.ratio[1])

    def display_raw_material_stock(self):
        print("============================")
        print("Raw Material Stock")
        print("============================")
        print("Raw Material")
        print(self.raw_qty)
        print("============================")

    def display_final_product_stock(self):

        print("==============================================")
        print("Final Product Stock")
        print("==============================================")
        print("Product Quantity")
        print(self.actual_product_qty)
        print("==============================================")


raw_qty = int(input("Enter the raw material qty:="))
ratio = input("Enter the ratio:=")
actual_product = input("Enter the actual product name:=")

c1 = manufacturing(raw_qty, ratio.split(':'), actual_product)

while True:
    print("1.Purchase Raw Material Product")
    print("2.Manufacture Actual Product")
    print("3.Show Raw Material Quantity")
    print("4.Show Actual Product Quantity")
    print("5.Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        c1.purchase_raw_material()
    elif choice == 2:
        c1.produce()
    elif choice == 3:
        c1.display_raw_material_stock()
    elif choice == 4:
        c1.display_final_product_stock()
    elif choice == 5:
        break
    else:
        print("Wrong Choice")
