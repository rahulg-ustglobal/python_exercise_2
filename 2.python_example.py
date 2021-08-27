"""
Write a program which extends Program - 1
Add appropriate class and perform inheritance
Add the facility of scrapping the raw material product and actual product
Add appropriate option in the menu for
○ scrapping the raw material product
○ scrapping the actual product
● Add appropriate methods to scrap the raw material product and actual
product
"""

class manufacturing:
    def __init__(self, raw_qty, ratio, actual_product):
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


class scrapping_material(manufacturing):
    def __init__(self, raw_qnty, ratio, actual_products):
        super().__init__(raw_qnty, ratio, actual_products)

    def scrap_final_product(self):
        self.actual_product_qty -= int(input("Enter the scrapping material:="))

    def scrap_raw_material_product(self):
        self.raw_qty -= int(input("Enter the scrapping material:="))

raw_qnty = int(input("Enter the raw material qty:="))
ratio = input("Enter the ratio:=")
actual_products = input("Enter the actual product name:=")

c1 = scrapping_material(raw_qnty, ratio.split(':'), actual_products)

while True:
    print("1.Purchase Raw Material Product")
    print("2.Manufacture Actual Product")
    print("3.Show Raw Material Quantity")
    print("4.Show Actual Product Quantity")
    print("5.Scrapping the raw material product")
    print("6.Scrapping the actual product")
    print("7.Exit")

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
        c1.scrap_raw_material_product()
    elif choice == 6:
        c1.scrap_final_product()
    elif choice == 7:
        break
    else:
        print("Wrong Choice")
