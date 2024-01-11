from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Review, Comment, Ingredient, Utensil, CuisineType
from django.contrib.admin.sites import AdminSite
from django.test.client import RequestFactory

from ..admin import PostAdmin, CommentAdmin

class AdminTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='chris',
            password='newpassword123',
            email='admin@example.com'
        )

        self.ingredient = Ingredient.objects.create(name='Test Ingredient')
        self.utensil = Utensil.objects.create(name='Test Utensil')
        self.cuisine_type = CuisineType.objects.create(name='Test Cuisine Type')

        self.review = Review.objects.create(
            title='Test Review',
            recipe='Test Recipe',
            content='Test Content',
            author=self.user,
            status=0 
        )

        self.comment = Comment.objects.create(
            name='Test Commenter',
            body='Test Comment Body',
            review=self.review
        )

        self.factory = RequestFactory()

    def test_review_admin(self):
        admin_site = AdminSite()

        request = self.factory.get('/admin/')
        request.user = self.user

        post_admin = PostAdmin(Review, admin_site)

        self.assertEqual(post_admin.prepopulated_fields, {'slug': ('recipe',)})

        self.assertEqual(post_admin.list_filter, ('status', 'created_on'))

        self.assertEqual(post_admin.list_display, ('title', 'recipe', 'slug', 'status', 'created_on'))

        self.assertEqual(post_admin.search_fields, ['title', 'recipe', 'content', 'email'])

        self.assertEqual(post_admin.summernote_fields, ("content"))

        self.assertEqual(post_admin.actions, ['approve_reviews'])

        post_admin.approve_reviews(request=request, queryset=Review.objects.filter(pk=self.review.pk))
        self.review.refresh_from_db()
        self.assertEqual(self.review.status, 1)

    def test_comment_admin(self):
        admin_site = AdminSite()

        request = self.factory.get('/admin/')
        request.user = self.user

        comment_admin = CommentAdmin(Comment, admin_site)

        self.assertEqual(comment_admin.list_display, ('name', 'body', 'created_on', 'approved', 'review'))

        self.assertEqual(comment_admin.list_filter, ('approved', 'created_on', 'review'))

        self.assertEqual(comment_admin.search_fields, ('name', 'address', 'body'))

        self.assertEqual(comment_admin.actions, ['approve_comments'])

        comment_admin.approve_comments(request=request, queryset=Comment.objects.filter(pk=self.comment.pk))
        self.comment.refresh_from_db()
        self.assertTrue(self.comment.approved)