import ipdb

class Food:
    
    all = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Food.all.append(self)

    @classmethod
    def food_names(cls):
        return [element.name for element in cls.all]

    @classmethod
    def average_price(cls):
        price_list = [element.price for element in cls.all]
        return sum(price_list) / len(price_list)
    
    # Bonus
    @classmethod
    def most_expensive(cls):
    # One possible algorithm to solve without using max()

        # most_expensive_food = None
        # for element in cls.all:
        #     if most_expensive_food == None:
        #         most_expensive_food = element
        #     else:
        #         if element.price > most_expensive_food.price:
        #             most_expensive_food = element

        # return most_expensive_food
                
    # Using the max() function  
        if len(cls.all) == 0:
            return None
        else:
            return max(cls.all, key=lambda f: f.price)

ipdb.set_trace()