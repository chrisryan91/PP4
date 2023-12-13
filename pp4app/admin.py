from django.contrib import admin
from .models import Review, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Review)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content', 'email']
    summernote_fields = ("content")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'created_on', 'approved', 'review')
    list_filter = ('approved', 'created_on', 'review')
    search_fields = ('name', 'address', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)