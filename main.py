class FlowerShop:
    def __init__(self):
        self.flowers = {}

    def add_flower(self, name, price):
        self.flowers[name] = price

    def get_price(self, name):
        return self.flowers.get(name, "Mavjud emas")

shop = FlowerShop()
shop.add_flower("Atirgul", 15000)
shop.add_flower("Lola", 10000)

print(shop.get_price("Atirgul"))
