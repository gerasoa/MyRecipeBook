from django.contrib import admin
from .models import Recipe , Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'steps', 'description',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('author', 'recipe', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)