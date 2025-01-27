from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'steps',)


# Register your models here.
# class RecipeAdmin(admin.ModelAdmin):
#      ordering = ('-created_on',)
#      list_filter = ('status', 'created_on')
#      list_display = ('title', 'author', 'status', 'created_on')

# admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(Comment)