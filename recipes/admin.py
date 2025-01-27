from django.contrib import admin
from .models import Recipe, Comment


# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
     ordering = ('-created_on',)
     list_filter = ('status', 'created_on')
     list_display = ('title', 'author', 'status', 'created_on')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment)