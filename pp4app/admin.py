from django.contrib import admin
from .models import Review, Comment, Ingredient, Utensil, CuisineType
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Ingredient)
admin.site.register(Utensil)
admin.site.register(CuisineType)


@admin.register(Review)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('recipe',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'recipe', 'slug', 'status', 'created_on')
    search_fields = ['title', 'recipe', 'content', 'email']
    summernote_fields = ("content")
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(status=1)

    approve_reviews.short_description = 'Approve selected reviews'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on', 'approved', 'review')
    list_filter = ('approved', 'created_on', 'review')
    search_fields = ('name', 'address', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
