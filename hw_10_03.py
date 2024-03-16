class Product:
    def __init__(self, name, calories, pfc):
        self.name = name
        self.calories = calories
        self.pfc = pfc

    def __str__(self):
        return self.name

class Meal:
    def __init__(self):
        self.products = []

    def add_product(self, product, weight):
        self.products.append((product, weight))

    def total_calories(self):
        total = 0
        for product, weight in self.products:
            total += (product.calories * weight) / 100
        return total

    def display_components(self):
        print("Meal components:")
        for product, weight in self.products:
            print(f"{product.name}: {weight}g")
        print(f'Total calories of meal: \n{self.total_calories()}')

meat = Product('meat', 250, (12, 5, 7))
apple = Product('apple', 30, (3, 4, 7))
dinner = Meal()
dinner.add_product(meat, 250)
dinner.add_product(apple, 75)
dinner.display_components()
