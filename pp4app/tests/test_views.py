from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from ..models import Review, Ingredient, Utensil

class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='PeterCollins', password='pragueprague')
        self.ingredient = Ingredient.objects.create(name='All Purpose Flour')
        self.utensil = Utensil.objects.create(name='Rolling Pin')


    def test_submit_review_view(self):
        self.client.login(username='PeterCollins', password='pragueprague')
        response = self.client.get(reverse('submit_review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit_review.html')

        response = self.client.post(reverse('submit_review'), {
            'title': 'Delicious Bread',
            'recipe': 'Batch Loaf',
            'slug': 'delicious_bread',
            'content': 'blah blah blah',
            'author': self.user.id,
            'ingredients': [self.ingredient.id],
            'utensils': [self.utensil.id],
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Review.objects.filter(title='Delicious Bread').exists())

        response = self.client.post(reverse('submit_review'), {
            'title': '',
            'recipe': 'Potato and Leek Soup',
            'slug': 'snail',
            'content': ' Blah blah blah',
            'author': self.user.id,
            'ingredients': [self.ingredient.id],
            'utensils': [self.utensil.id],
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'title', 'This field is required.')

    def test_reviews_view(self):
        review_a = Review.objects.create(title='Review A', recipe='Recipe A', author=self.user, status=1, slug='review-a')
        review_b = Review.objects.create(title='Review B', recipe='Recipe B', author=self.user, status=1, slug='review_b')

        self.assertIsNotNone(review_a)
        self.assertIsNotNone(review_b)

        url = reverse('reviews')
        response = self.client.get(url)

        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_blog.html')
        self.assertEqual(response.content.decode('utf-8').count('<div class="col-md-3">'), 2)

    def test_review_upvote_view(self):
        review = Review.objects.create(title='Potato and Leek Soup', recipe='Soup', slug='potato-and-leek-soup', author=self.user, status=1)

        self.client.login(username='PeterCollins', password='pragueprague')

        response = self.client.post(reverse('review_upvote', kwargs={'slug': review.slug}), {'vote_type': 'upvote'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(review.up_vote.filter(id=self.user.id).exists())

        response = self.client.post(reverse('review_upvote', kwargs={'slug': review.slug}), {'vote_type': 'downvote'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(review.down_vote.filter(id=self.user.id).exists())