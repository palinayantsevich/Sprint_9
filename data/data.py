from pathlib import Path


class RecipeData:
    RECIPE_NAME = 'Хлеб с маслом'
    INGREDIENTS = [
        ('хлеб', 500),
        ('сливочное масло', 20),
        ('розмарин', 2)
    ]

    TIME_VALUE = 15
    RECIPE_DESCRIPTION = 'Xлеб всему голова.'

    IMAGE_PATH = Path(__file__).resolve().parents[1] / "data" / "img" / "bread_and_butter.jpg"
