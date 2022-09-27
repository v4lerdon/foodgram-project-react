from django.contrib import admin

from recipes.models import (AmountOfIngredient, Favorite, Ingredient, Recipe,
                            ShoppingList, Tag)

admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(Favorite)
admin.site.register(ShoppingList)
admin.site.register(AmountOfIngredient)
