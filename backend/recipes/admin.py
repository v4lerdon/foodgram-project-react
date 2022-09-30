from django.contrib import admin

from recipes.models import (AmountOfIngredient, Favorite, Ingredient, Recipe,
                            ShoppingList, Tag)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'is_favorited')
    search_fields = ('name', 'author')
    list_filter = ('author', 'name', 'tags')

    def is_favorited(self, obj):
        return obj.favorites.count()


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Favorite)
admin.site.register(ShoppingList)
admin.site.register(AmountOfIngredient)
