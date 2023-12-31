class InventoryManagement:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        if item_name in self.inventory:
            print(f"{item_name} is already in the inventory. Use the update function to modify.")
        else:
            self.inventory[item_name] = {'quantity': quantity, 'price': price}
            print(f"{item_name} added to the inventory.")

    def update_item(self, item_name, quantity=None, price=None):
        if item_name in self.inventory:
            if quantity is not None:
                self.inventory[item_name]['quantity'] = quantity
            if price is not None:
                self.inventory[item_name]['price'] = price
            print(f"{item_name} updated.")
        else:
            print(f"{item_name} does not exist in the inventory.")

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"{item_name} removed from the inventory.")
        else:
            print(f"{item_name} does not exist in the inventory.")

    def generate_report(self):
        print("Current Inventory:")
        for item, data in self.inventory.items():
            print(f"Item: {item}, Quantity: {data['quantity']}, Price: {data['price']}")

# Usage example
inventory_manager = InventoryManagement()

inventory_manager.add_item('Apple', 100, 100)
inventory_manager.add_item('Banana', 150, 70)

inventory_manager.generate_report()

inventory_manager.update_item('Apple', quantity=50, price=1.2)

inventory_manager.remove_item('Banana')

inventory_manager.generate_report()
