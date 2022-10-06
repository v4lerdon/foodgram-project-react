from django_filters import rest_framework

from .models import Recipe


class RecipeFilter(rest_framework.FilterSet):
    # tags = rest_framework.AllValuesMultipleFilter(
    #     field_name='tags__slug',
    # )
    is_favorited = rest_framework.BooleanFilter(
        method='get_is_favorited'
    )
    is_in_shopping_cart = rest_framework.BooleanFilter(
        method='get_is_in_shopping_cart'
    )

    class Meta:
        model = Recipe
        fields = ('author', 'is_favorited', 'is_in_shopping_cart')

    def get_is_favorited(self, queryset, name, value):
        user = self.request.user
        if value is True:
            return queryset.filter(favorites__user__username=user)

    def get_is_in_shopping_cart(self, queryset, name, value):
        user = self.request.user
        if value:
            return queryset.filter(purchases__user__username=user)
        return Recipe.objects.all()
