class Device:
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False
    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} тепер працює.")
    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} вимкнено.")
class TV(Device):
    def __init__(self, brand, screen_size):
        super().__init__(brand)
        self.screen_size = screen_size
    def info(self):
        print(f"Це телевізор {self.brand}, діагональ: {self.screen_size} дюймів.")

class Smartphone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def info(self):
        print(f"Це смартфон {self.brand}, модель: {self.model}.")
my_tv = TV("Sasung", 55)
my_tv.info()
my_tv.turn_on()
print("-" * 20)
my_phone = Smartphone("Apule", "Phone 15")
my_phone.info()
my_phone.turn_off()