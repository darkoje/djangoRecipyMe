from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Foodpreparationtype


admin.site.register(Foodpreparationtype, MPTTModelAdmin)
