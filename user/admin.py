from django.contrib import admin
from  .models import CustomUser

@admin.register(CustomUser)
class User(admin.ModelAdmin):
    list_display = ('username','email', 'first_name', 'role')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email', 'role')