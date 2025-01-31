from django.contrib import admin
from django.contrib.auth.models import Group
from .models import ChefProfile

# Register your models here.
#admin.site.register(Chef)


@admin.register(ChefProfile)
class ChefAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

# admin.site.register(ChefProfile)
admin.site.unregister(Group)