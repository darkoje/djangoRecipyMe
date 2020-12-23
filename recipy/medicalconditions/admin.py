from django.contrib import admin
from .models import MedicalConditionsGroup, MedicalConditions


class MedicalConditionsGroupAdmin(admin.ModelAdmin):
    list_display = ('group',)

class MedicalConditionsAdmin(admin.ModelAdmin):
    list_display = ('name','group',)

admin.site.register(MedicalConditionsGroup,MedicalConditionsGroupAdmin)
admin.site.register(MedicalConditions, MedicalConditionsAdmin)
