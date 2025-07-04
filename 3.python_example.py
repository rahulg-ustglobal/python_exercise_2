"""
Program - 3
● Write a program which is having a class InventoryManagement.
● System should manage the quantity of purchase and sales processes.
● If the system is not having enough quantity during sales, the system should show a
warning message “Not enough product quantities to sell”.
Write appropriate constructor, methods to manage the sales and purchase
processes.
● There should be a provision to view the available quantities.
● This should be a menu driven program, which allows to
○ Purchase Product
○ Sale Product
○ View Available Product Quantities
○ Exit
● Whenever sales take place, the system should process the quantities and then
should show the available quantities.
"""

class inventory_Management:
    def __init__(self):
        self.product = {"quantity": 0}

    def purchase_quantity_product(self):
        purchase_quantity = int(input("Enter the purchase no:="))
        self.product["quantity"] += purchase_quantity
        print("===========================")
        print("Purchased quantity")
        print("===========================")
        print(self.product.get("quantity"))
        print("===========================")

    def sales_processes_product(self):
        purchase_product = int(input("Enter the sales no:="))
        if purchase_product > self.product["quantity"]:
            print("Not enough product quantities to sell")
        else:
            self.product["quantity"] = self.product["quantity"] - purchase_product
            print("===========================")
            print("Purchase quantity")
            print("===========================")
            print(self.product.get("quantity"))
            print("===========================")

    def available_product(self):
        print("===========================")
        print("Available product quantity")
        print("===========================")
        print(self.product.get("quantity"))
        print("===========================")


c1 = inventory_Management()

while True:
    print("1.Purchase Product")
    print("2.Sale Product")
    print("3.View Available Product Quantities")
    print("4.Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        c1.purchase_quantity_product()
    elif choice == 2:
        c1.sales_processes_product()
    elif choice == 3:
        c1.available_product()
    elif choice == 4:
        break
    else:
        print("Wrong Choice")
