from django.contrib import admin
from django.contrib.auth.models import Group
from .models import ChefProfile


@admin.register(ChefProfile)
class ChefAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ChefProfile model.

    Displays user, name, and last update in the list view.
    Prepopulates the slug field based on the name.
    Sets the displayed fields in the admin form.
    """
    list_display = ('user', 'name', 'updated_on')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('user', 'name', 'slug', 'bio', 'photo_small', 'photo_large')


admin.site.unregister(Group)
