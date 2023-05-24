# Req 3
from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.items = self.load(source_path)
        self.dishes = self.add()

    def load(self, path: str):
        with open(path) as file:
            content = csv.DictReader(file)

            return list(content)

    def add(self):
        menu_content = {}

        for item in self.items:
            dish = Dish(item["dish"], float(item["price"]))

            ingredient = Ingredient(item["ingredient"])

            quantity = int(item["recipe_amount"])

            if dish not in menu_content:
                menu_content[dish] = dish

            menu_content[dish].add_ingredient_dependency(
                ingredient, quantity
            )

        result = []

        for value in menu_content.values():
            result.append(value)

        return result
