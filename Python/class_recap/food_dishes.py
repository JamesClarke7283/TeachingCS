"""Classes of food dishes

This module contains a class for food dishes.

Classes:
    FoodDish: A class for food dishes.

    Functions:
        get_food_dish: Returns a food dish name.
"""


class FoodDish:

    def __init__(self, name: str, price: float, ingredients: list[str]):
        self.__name: str = name
        self.__price: float = price
        self.__ingredients: list[str] = ingredients

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients: list[str]):
        self.__ingredients = ingredients

    def __repr__(self):
        output = f"{self.name} - Price: ${self.price}:"
        output += "\n\tIngredients:"
        for ingredient in self.__ingredients:
            output += f"\n-\t{ingredient}"
        return output


class TunaAndSpices(FoodDish):
    def __init__(self, price: float):
        super().__init__("Tuna with Spices", price, ["Tuna Fish", "Spices"])


class FishAndChips(FoodDish):
    def __init__(self, price: float, added_ingredients: list[str], waiter_name):
        ingredients = ["Fish", "Chips"]
        ingredients.extend(added_ingredients)
        super().__init__("Fish and Chips", price, ingredients)
        self.__waiter: str = waiter_name

    @property
    def waiter_name(self):
        return self.__waiter

    @waiter_name.setter
    def waiter_name(self, waiter_name: str):
        # Checks if waiter name is in title case
        if waiter_name == waiter_name.title():
            self.__waiter = waiter_name
        else:
            raise ValueError("Waiter name must be in title case")

    def __repr__(self):
        output = super().__repr__()
        output += f"\n\tWaiter: {self.waiter_name}"
        return output


def main():
    """Main function"""
    tas = TunaAndSpices(5)
    fas = FishAndChips(4, ["Salt", "Pepper"], "John")
    print(tas)
    print(fas)


if __name__ == "__main__":
    main()
