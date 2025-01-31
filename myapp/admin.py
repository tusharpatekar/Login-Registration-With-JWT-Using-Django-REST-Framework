from django.contrib import admin

# Register your models here.

from myapp.models import *

admin.site.register(Role)
admin.site.register(UserRole)