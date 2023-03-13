from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework import routers
from .views import (
    IngredientViewSet,
    TagViewSet,
    RecipeViewSet, FavoriteViewSet, ShoppingViewSet
)

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'favorite', FavoriteViewSet, basename='favorite')
router.register(r'shopping', ShoppingViewSet, basename='shopping')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'users', UserViewSet, basename='users')
router.register(
    r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
    path(r'auth/', include('djoser.urls.authtoken')),
]
