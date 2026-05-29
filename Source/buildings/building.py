class Building:
    def __init__(self):
        self.owner = ""
        self.workers = {}
        self.stock = {}
        self.schedule = {}
        self.current_stock = self.stock

    def subtract_stock(self, item, amount = 1):
        if not self.current_stock.get(item):
            return
        item_quantity = self.current_stock.get(item) - amount

        if item_quantity < 0:
            print("Not enough stock. Come back tommorow.")
        else:
            self.current_stock[item] = item_quantity
    def refresh_stock(self):
        self.current_stock = self.stock

    #TODO: make helper method to check if shop is open or closed 
    #alchemist shop
