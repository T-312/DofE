# Product Inventory Project - Create an application which manages an inventory of products. 
# Create a product class which has a price, id, and quantity on hand. 
# Then create an inventory class which keeps track of various products and can sum up the inventory value.

class Product:
    def __init__(self, id, price, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity

    def __str__(self):
        return self.id + ' ' + self.price + ' ' + self.quantity

class Inventory:
    def show_inventory(self):
        inventory_value = 0
        for i in stock:
            inventory_value+=int(int(i.price) * int(i.quantity))

        print(inventory_value)

stock = [Product("Banana", "10", "157"),
         Product("Apple", "5", "112"),
         Product("Yogurt", "15", "67")]

Inventory().show_inventory()