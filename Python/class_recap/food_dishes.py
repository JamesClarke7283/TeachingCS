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
        output = f"{self.name} - {self.price}:"
        output += "\n\tIngredients:"
        for ingredient in self.__ingredients:
            output += f"\n-\t{ingredient}"
        return output


class TunaAndSpices(FoodDish):
    def __init__(self, price: float):
        super().__init__("Tuna with Spices", price, ["Tuna Fish", "Spices"])


def main():
    """Main function"""
    tas = TunaAndSpices(10)
    print(tas)


if __name__ == "__main__":
    main()
