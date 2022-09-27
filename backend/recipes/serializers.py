from django.forms import ValidationError
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueTogetherValidator

from recipes.models import (AmountOfIngredient, Favorite, Ingredient, Recipe,
                            ShoppingList, Tag)


class IngredientSerializer(serializers.ModelSerializer):
    """Сериализация ингредиентов."""

    class Meta:
        model = Ingredient
        fields = '__all__'


class AmountOfIngredientSerializer(serializers.ModelSerializer):
    """Сериализация количества ингредиентов."""
    id = serializers.PrimaryKeyRelatedField(
        source='ingredient',
        read_only=True
    )
    name = serializers.SlugRelatedField(
        slug_field='name',
        source='ingredient',
        read_only=True
    )
    measure = serializers.SlugRelatedField(
        slug_field='measure',
        source='ingredient', read_only=True
    )

    class Meta:
        model = AmountOfIngredient
        fields = '__all__'


class AddAmountOfIngredientSerializer(serializers.ModelSerializer):
    """Сериализация добавления количества ингредиентов."""
    id = serializers.PrimaryKeyRelatedField(
        source='ingredient',
        queryset=Ingredient.objects.all()
    )
    amount = serializers.IntegerField()

    class Meta:
        model = AmountOfIngredient
        fields = ('amount', 'id')


class TagSerializer(serializers.ModelSerializer):
    """Сериализация тэгов."""

    class Meta:
        model = Tag
        fields = ('__all__')
        lookup_field = 'id'
        extra_kwargs = {'url': {'lookup_field': 'id'}}


class RecipeSerializer(serializers.ModelSerializer):
    """Сериализация рецептов."""

    class Meta:
        model = Recipe
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    """Сериализация избранного."""

    class Meta:
        model = Favorite
        fields = ('user', 'recipe')
        validators = [
            UniqueTogetherValidator(
                queryset=Favorite.objects.all(),
                fields=('user', 'recipe'),
                message='Рецепт уже в избранном'
            )
        ]


class ShoppingListSerializer(FavoriteSerializer):
    """Сериализация списка ппокупок."""

    class Meta:
        model = ShoppingList
        fields = ('user', 'recipe')
        validators = [
            UniqueTogetherValidator(
                queryset=ShoppingList.objects.all(),
                fields=('user', 'recipe'),
                message='Рецепт уже в списке покупок'
            )
        ]
