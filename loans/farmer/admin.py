from django.contrib import admin

# Register your models here.
from .models import FarmerWealth
from .models import Farmer

admin.site.register(Farmer)
admin.site.register(FarmerWealth)