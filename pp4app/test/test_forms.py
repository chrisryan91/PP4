from django.test import TestCase
from pp4app.forms import CommentForms, ReviewForm
from pp4app.models import Comment, Ingredient, Utensil, CuisineType
from django.contrib.auth.models import User
import unittest

class ReviewFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.ingredient = Ingredient.objects.create(name='Ingredient 1')
        self.utensil = Utensil.objects.create(name='Utensil 1')
        self.cuisine_type = CuisineType.objects.create(name='Italian')

    def test_review_form_valid_data(self):

        data = {
            'title': 'Delicious Recipe',
            'recipe': 'Test Recipe',
            'content': 'This is a delicious recipe!',
            'cuisine_type': [self.cuisine_type.id],
            'new_ingredient': 'Butter',
            'featured_image_a': 'path/to/image.jpg',
            'prep_time': 30,
            'url': 'https://example.com',
            'ingredients': [self.ingredient.id],
            'utensils': [self.utensil.id],
        }

        form = ReviewForm(data=data)

        if not form.is_valid():
            print(form.errors)

        self.assertTrue(form.is_valid(), f"Form errors: {form.errors}")
        
        self.assertTrue(form.is_valid())

    def test_review_form_empty_data(self):
        data = {}

        form = ReviewForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertIn('recipe', form.errors.keys())
        self.assertIn('content', form.errors.keys())
        self.assertNotIn('new_ingredient', form.errors.keys())


    def test_review_form_invalid_data(self):
        form = ReviewForm(data={'title': 'Test Review', 'recipe': 'Test Recipe'})

        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())

    def test_review_form_save_method(self):
        data = {
            'title': 'Delicious Recipe',
            'recipe': 'Test Recipe',
            'content': 'This is a delicious recipe!',
            'ingredients': [self.ingredient.id],
            'utensils': [self.utensil.id],
            'cuisine_type': [self.cuisine_type.id],
        }

        self.client.login(username='testuser', password='testpassword')
        form = ReviewForm(data=data)

        self.assertTrue(form.is_valid())
        self.assertNotIn('content', form.errors.keys())
        if not form.is_valid():
            print(form.errors)

        review_instance = form.save(user=self.user)

        self.assertEqual(review_instance.title, 'Delicious Recipe')
        self.assertEqual(review_instance.recipe, 'Test Recipe')
        self.assertEqual(review_instance.content, 'This is a delicious recipe!')
        self.assertEqual(review_instance.slug, 'delicious-recipe')

        self.client.logout

if __name__ == '__main__':
    unittest.main()

class CommentFormsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Richard', password='chess')

    def test_comment_form_valid_data(self):
        data = {'body': '... blah blah blah... '}

        form = CommentForms(data=data)
        self.assertTrue(form.is_valid())

    def test_comment_form_empty_data(self):
        data = {}
        form = CommentForms(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_comment_form_body_max_length(self):
        long_body = 'a' * (Comment.body.field.max_length + 1)
        data = {'body': long_body}

        form = CommentForms(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())

if __name__ == '__main__':
    unittest.main()