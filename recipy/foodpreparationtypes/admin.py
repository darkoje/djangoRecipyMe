from django.contrib import admin
from .models import FoodPreparationTypeCategory, FoodpreparationType

class FoodpreparationTypeAdmin(admin.ModelAdmin):
    list_display = ('name','description','category',)

class FoodPreparationTypeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(FoodPreparationTypeCategory,FoodPreparationTypeCategoryAdmin)
admin.site.register(FoodpreparationType, FoodpreparationTypeAdmin)
