class Item:
    def __init__(self, id, name, price, stock=0):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"id: {self.id} name: {self.name} price: £{self.price} stock: {self.stock}"

    def get_item(self):
        return {"id": self.id, "name": self.name, "price": self.price, "stock": self.stock}


class Store:
    def __init__(self, items=[]):
        self.items = items

    def __repr__(self):
        l = len(self.items)
        if l == 1:
            return f"There is {l} item available at the moment"
        else:
            return f"There are {l} different items available at the moment"

    def add_item(self, item):
        item_to_add = Item(item.id, item.name, item.price, item.stock)
        self.items.append(item_to_add.get_item())

    def view_items(self):
        return self.items

    def update_item_name(self, item_id, new_name):
        for item in self.items:
            print(item)
            if item["id"] == item_id:
                item["name"] = new_name
                break

    def update_item_price(self, item_id, new_price):
        for item in self.items:
            if item["id"] == item_id:
                item["price"] = new_price
                break

    def update_item_stock(self, item_id, new_stock):
        for item in self.items:
            if item["id"] == item_id:
                item["stock"] = new_stock
                break

    def delete_item(self, item_id):
        self.items = [d for d in self.items if d['id'] != item_id]

    def check_stock(self, item_id):
        for item in self.items:
            if item["id"] == item_id:
                print("item: ", item)
                return f"There are " + str(item["stock"]) + " item(s) of " + item["name"] + " are available"

    def total_value(self):
        total = 0
        for item in self.items:
            total += item["price"] * item["stock"]
        return total


item1 = Item(1, "pen", 2, 30)
item2 = Item(2, "cup", 5, 20)
print(item1)
store = Store()
print(store)
store.add_item(item1)
print(store)
store.add_item(item2)
print(store)
print(store.view_items())
store.update_item_name(1, "pencil")
print(store.view_items())

store.update_item_price(2, 10)
store.update_item_stock(2, 100)
print(store)

item3 = Item(3, "coffee", 15, 200)
store.add_item(item3)
print(store.view_items())

store.delete_item(1)
print(store.view_items())
print(store.check_stock(2))

print(store.total_value())
