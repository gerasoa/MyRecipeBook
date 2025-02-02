from django.contrib import admin
from django.contrib.auth.models import Group
from .models import ChefProfile

# Register your models here.
#admin.site.register(Chef)


@admin.register(ChefProfile)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'updated_on')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('user', 'name', 'slug', 'bio', 'photo_small', 'photo_large')

# admin.site.register(ChefProfile)
admin.site.unregister(Group)