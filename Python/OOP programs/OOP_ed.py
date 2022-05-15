class Car:
    discount = 50

    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    def full_name(self):
        return f'{self.brand} {self.model}'

    def anniversary_discount(self):
        self.price = self.price - (self.price*self.discount/100)

    def display_stock(self):
        pass

audi = Car("Audi", "R8", "Red", 1000000)
audi.anniversary_discount()


print(audi.price)