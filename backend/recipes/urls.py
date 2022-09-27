from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import IngredientViewSet, TagViewSet

app_name = 'recipes'

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register('tags', TagViewSet, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
]
