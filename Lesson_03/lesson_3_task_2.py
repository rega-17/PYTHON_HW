class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

catalog = [
    Smartphone("Samsung", "Galaxy S21", "+79161111111"),
    Smartphone("Apple", "iPhone 13", "+79162222222"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79163333333"),
    Smartphone("Google", "Pixel 6", "+79164444444"),
    Smartphone("OnePlus", "9 Pro", "+79165555555")
]

# Цикл для печати всего каталога
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")