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
router.register(r'recipes/${id}/favorites/', FavoriteViewSet, basename='recipes')
router.register(r'recipes/${id}/shopping_cart/', ShoppingCartViewSet, basename='recipes')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'users', CustomUserViewSet, basename='users')
router.register(
    r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
    path(r'auth/', include('djoser.urls.authtoken')),
]
