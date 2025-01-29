from django.contrib import admin
from .models import Chef

# Register your models here.
#admin.site.register(Chef)


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}