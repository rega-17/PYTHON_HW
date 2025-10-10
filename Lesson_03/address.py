class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def display_address(self):
        print(f"Индекс: {self.index}")
        print(f"Город: {self.city}")
        print(f"Улица: {self.street}")
        print(f"Дом: {self.house}")
        print(f"Квартира: {self.apartment}")

    def get_full_address(self):
        return f"{self.index}, {self.city}, {self.street}, {self.house}, {self.apartment}"


addr = Address("123456", "Москва", "Ленина", "10", "25")
addr.display_address()
print(addr.get_full_address())