from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Recipe model.

    Enables Summernote rich text editing for selected fields.
    Displays basic recipe details and allows filtering and
    search in the admin list.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'steps', 'description',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Comment model.

    Displays comment details and allows approval via a custom admin action.
    Includes filters and search functionality in the comment list.
    """

    list_display = ('author', 'recipe', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Custom admin action to approve selected comments.

        Args:
            request (HttpRequest): The current admin request.
            queryset (QuerySet): The selected comments in the admin interface.
        """

        queryset.update(approved=True)
