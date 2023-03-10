from django.urls import path, include
from rest_framework import routers
from backend.api.views import IngredientViewSet, TagViewSet, RecipeViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register('ingredients', IngredientViewSet)
router.register('tags', TagViewSet)
router.register('recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
