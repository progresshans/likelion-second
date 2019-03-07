from django.contrib import admin

# Register your models here.
from .models import Blog, Portfolio

admin.site.register(Blog)
admin.site.register(Portfolio)