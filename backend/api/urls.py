from django.urls import path, include
from rest_framework import routers
from .views import (
    IngredientViewSet,
    TagViewSet,
    RecipeViewSet,
    CustomUserViewSet,
    FavoriteViewSet,
    ShoppingCartViewSet
)

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'recipes/(?P<recipes_id>\d+)/favorite', FavoriteViewSet, basename='favorites')
router.register(r'recipes/(?P<recipes_id>\d+)/shopping_cart', ShoppingCartViewSet, basename='shopping_cart')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'users', CustomUserViewSet, basename='users')
router.register(
    r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
    path(r'auth/', include('djoser.urls.authtoken')),
]
