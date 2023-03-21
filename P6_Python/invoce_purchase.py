"""Develop a program to generate invoices to customers and purchase orders from suppliers.
The system displays a menu asking if you want to make an invoice or purchase order
In case of an invoice, it asks for the client’s data  and in case of being PO enter the supplier’s data.
Then the program asks to enter up to 10 items (may be less) with description and its value

At the end it calculates the net, GST, and finally shows on screen all the data of the invoice (or PO). 
One thing per line:
Invoice Number (PO)
Customer number (Supplier)
Customer name (Supplier)
————————
Items with the value of each
———————- 
Net
GST
PST
Total"""

import string
import random

class Client:
    def __init__(self, *args):
        self.name = ""
        self.number = ""
        self.phone = ""
        if (len(args) == 2):
            self.name = args[0]
            self.phone = args[1]
        self.generate_number()

    def get_name(self):
        return self.name
        
    def generate_number (self):
        chars = string.ascii_uppercase + string.digits
        self.number = ''.join(random.choice(chars) for _ in range(6))

    def get_number(self):
        return self.number 
    
    def get_phone(self):
        return self.phone

class Purchase:
    def __init__(self, client):
        self.client = client
        self.generate_invoice_number()
        self.list_suppliers = []
        self.purchase_total = 0.0
        self.net_price = 0.0 
        self.gst = 0.0
 
    def generate_invoice_number (self):
        chars = string.ascii_uppercase + string.digits
        self.invoice_number = ''.join(random.choice(chars) for _ in range(3))
        print(f"\nInvoice number: {self.invoice_number}")
        
    def get_invoice_number(self):
        return self.invoice_number

    def suppliers_data(self, quantity):
        order = 0

        while order < quantity:
            dic ={}
            order += 1

            product = input(f"\nPlease, insert the product {order}: ")
            dic["Product"] = product
            
            description = input(f"Please, insert the description of product {order}: ")
            dic["Description"] = description
            
            value = float(input(f"Please, insert the value of product {order}: "))
            dic["Value"] = value 
            
            self.list_suppliers.append(dic)
        self.finish_purchase()
        
    def get_client_number(self):
        return self.client.get_number()
    
    def get_client_name(self):
        return self.client.get_client_name()

    def calc_total(self):
        total = 0
        for product in self.list_suppliers:
            value_product = product["Value"]
            total += value_product
        self.purchase_total = total
    
    def calc_gst(self):
        self.gst = self.purchase_total * (5/100)
    
    def calc_net_price(self):
        self.net_price = self.purchase_total + self.gst

    def finish_purchase(self):
        self.calc_total()
        self.calc_gst()
        self.calc_net_price()

    def invoice_data(self):
        print("\nInvoice number: ", self.get_invoice_number())
        print("Client number: ", self.client.get_number())
        print("Client name: ", self.client.get_name(), "\n")

        print("Items whith the value: ")
        for p in self.list_suppliers:
            print(f"{p['Product']}: {p['Value']}")
        print("\nGST: ", self.gst)
        print("NET: ", self.net_price)
        print("Total of purchase: ", self.purchase_total)

class Main:
    def __init__(self):
        self.list_purchases = []
        self.list_clients = []

    def add_client(self, name, phone):  
        for c in self.list_clients:
            if c.get_name() == name and c.get_phone() == phone:
                return c
        c = Client(name, phone)
        self.list_clients.append(c)
        return c

    def list_new_purchase(self, number, quantity): 
        for c in self.list_clients:
            if c.get_number() == number:
                client = c
                break

        p = Purchase(client)
        p.suppliers_data(quantity)
        self.list_purchases.append(p)

    def search_purchase(self, invoice_number):
        for p in self.list_purchases:
            if p.get_invoice_number() == invoice_number:
                p.invoice_data()
                return
        print("Purchase not found.")

main = Main()

while True:
    print("\nMenu options:  ")
    print("1 - Purchase order")
    print("2 - Invoice")
    print("3 - Quit\n")

    action = int(input("Option: "))

    if action == 3:
        print("\nThank you for buying with us.")
        break
    
    client_name = input("Please, insert the client name: ")
    client_phone = input("Please, insert the client phone: ")

    if action == 1:
        client = main.add_client(client_name, client_phone)
        client_number = client.get_number()
        quantity = int(input("You can enter up to 10 items. How many items do you want to do the purchase? "))
        main.list_new_purchase(client_number, quantity)
    elif action == 2:
        purchase_number = input("Please, insert the purchase number: ")
        main.search_purchase(purchase_number)

        


