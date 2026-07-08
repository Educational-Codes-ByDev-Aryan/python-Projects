# Task Online Shopping Cart
class ShoppingCart:
    def __init__(self):
         self.__total_price = 0

    def get_total(self):
         return self.__total_price

    def add_item(self,price):
         if price > 0 :

             self.__total_price = self.__total_price + price
         else:
              print("Invalid Price")

    def remove_item(self,price):
         if price > 0 and  price <= self.__total_price:
              self.__total_price-=price
         else:
              print("Invalid price")

cart = ShoppingCart()
print(cart.get_total())

cart.add_item(900)
print(cart.get_total())

cart.add_item(900)
print(cart.get_total())

cart.add_item(900)
print(cart.get_total())

cart.remove_item(900)
print(cart.get_total())
