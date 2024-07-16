# Перенесите сюда свой код из прошлой домашки и продолжите работу с ним
class Product:
    """
    Класс для описания товара в магазине
    """

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __len__(self):
        return len(self.quantity)

    def __add__(self, other):
        if type(other) is Product:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, product):
        name, description, price, quantity = product.values()
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        Product.price = new_price


class Category:
    """
    Класс для категорий товара
    """
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        total_products_count = []
        for i in self.__products:
            total_products_count.append(i.quantity)
        return f'{self.name}, количество продуктов: {sum(total_products_count)} шт.'

    @property
    def products(self):
        products_str = ''
        for product in self.__products:
            products_str += f'{str(product)}\n'
        return products_str

    @products.setter
    def products(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError('Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)')


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)