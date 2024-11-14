class Smartphone:

    def __init__(self, brand, model, numder):
        self.brand = brand
        self.model = model
        self.num = numder

    def get_smartphone(self):
        return f'{self.brand} - {self.model}. {self.num}'
