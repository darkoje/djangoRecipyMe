from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Ingredient, Category

class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'energy', 'protein', 'fats', 'saturated_fatty_acids', 'carbohydrates', 'sugars', 'sodium', 'fiber')

admin.site.register(Ingredient,IngredientsAdmin)
admin.site.register(Category, MPTTModelAdmin)
