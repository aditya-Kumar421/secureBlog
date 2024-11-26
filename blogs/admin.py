from django.contrib import admin
from .models import Blog
# Register your models here.

@admin.register(Blog)
class User(admin.ModelAdmin):
    list_display = ('title','created_date', 'user')
    list_filter = ('title', 'created_date')
    search_fields = ('title', 'created_date')