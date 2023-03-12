from django.contrib import admin

from .models import (
    Recipe,
    Ingredient,
    Tag,
    IngredientInRecipe,
    ShoppingCart,
    Favourite
)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'author',)

    list_filter = ('author', 'name', 'tags',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color_tag', 'slug',)


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)


class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)


class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Favourite, FavouriteAdmin)
admin.site.register(IngredientInRecipe, IngredientInRecipeAdmin)
