from django.contrib import admin
from .models import Drug
# Register your models here.

admin.site.register(Drug)
from .models import Prescriber

# Register your models here.

admin.site.register(Prescriber)
