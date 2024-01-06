from django.test import TestCase
from ..models import Review, Ingredient, Utensil, Comment, CuisineType
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

class IngredientModelTest(TestCase):
    def test_ingredient_str_representation(self):
        ingredient = Ingredient(name='Tomato')

        expected_str = 'Tomato'
        self.assertEqual(str(ingredient), expected_str)

class UtensilModelTest(TestCase):
    def test_utensil_str_representation(self):
        utensil = Utensil(name='Spatula')

        expected_str = 'Spatula'
        self.assertEqual(str(utensil), expected_str)

class CuisineTypeModelTest(TestCase):
    def test_cuisine_type_str_representation(self):
        cuisine_type = CuisineType(name='Italian', slug='italian')

        expected_str = 'Italian'
        self.assertEqual(str(cuisine_type), expected_str)

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='mark', password='patterson')
        self.ingredient = Ingredient.objects.create(name='Asparagus')
        self.utensil = Utensil.objects.create(name='Wok')
        self.review = Review.objects.create(
            title='Delicious Stir Fry',
            recipe='Stir Fry',
            slug=slugify('Stir Fry'),
            author=self.user,
            content='... blah blah blah...',
            prep_time=10
        )

        self.second_review = Review.objects.create(
            title='Another Delicious Stir Fry',
            recipe='Another Stir Fry',
            slug=slugify('Another Stir Fry'),
            author=self.user,
            content='... blah blah blah...',
            prep_time=10,
            created_on=self.review.created_on + timedelta(seconds=1)
        )

    def test_review_creation(self):
        self.assertEqual(self.review.title, 'Delicious Stir Fry')
        self.assertEqual(self.review.recipe, 'Stir Fry')
        self.assertEqual(self.review.author, self.user)
        self.assertEqual(self.review.content, '... blah blah blah...')
        self.assertEqual(self.review.prep_time, 10)
        self.assertIn(self.review.status, [0, 1])

    def test_ordering(self):
        reviews = Review.objects.all()
        self.assertGreaterEqual(reviews[0].created_on, reviews[1].created_on)

    def test_review_upvote(self):
        second_user = User.objects.create_user(username='MarkP', password='malahide')
        self.review.up_vote.add(self.user)
        self.review.up_vote.add(second_user)

        self.assertEqual(self.review.number_of_up_votes(), 2)
    
    def test_number_of_down_votes(self):
        second_user = User.objects.create_user(username='Sean', password='gambling')
        self.review.down_vote.add(self.user)
        self.review.down_vote.add(second_user)

        self.assertEqual(self.review.number_of_down_votes(), 2)

    def test_total_votes(self):
        second_user = User.objects.create_user(username='Sean', password='gambling')
        self.review.up_vote.add(self.user)
        self.review.down_vote.add(second_user)

        self.assertEqual(self.review.total_votes(), 0)

    def test_str_method(self):
        self.assertEqual(str(self.review), 'Delicious Stir Fry')

    def test_get_absolute_url(self):
        expected_url = f'/review/{self.review.slug}/'
        self.assertEqual(self.review.get_absolute_url(), expected_url)

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Alice', password='wonderland')
        self.ingredient = Ingredient.objects.create(name='Asparagus')
        self.utensil = Utensil.objects.create(name='Wok')
        self.review = Review.objects.create(
            title='Delicious Stir Fry',
            recipe='Stir Fry',
            slug=slugify('Delicious Stir Fry'),
            author=self.user,
            content='... blah blah blah...',
            prep_time=10
        )

    def test_comment_creation(self):
        comment_data = {
            'review': self.review,
            'name': 'Joe Doe',
            'email': 'joedoe@example.com',
            'body': 'Brutal recipe - unedible',
        }

        comment = Comment.objects.create(**comment_data)

        self.assertEqual(comment.review, self.review)
        self.assertEqual(comment.name, 'Joe Doe')
        self.assertEqual(comment.email, 'joedoe@example.com')
        self.assertEqual(comment.body, 'Brutal recipe - unedible')
        self.assertFalse(comment.approved)

        comments_for_review = Comment.objects.filter(review=self.review)
        self.assertEqual(list(comments_for_review), [comment])

    def test_comment_str_representation(self):
        comment = Comment(
            review=None,
            name='Joe Doe',
            email='joedoe@example.com',
            body='Worst recipe ever'
        )

        # Check the __str__ representation
        expected_str = f"Comment {comment.body} by {comment.name}"
        self.assertEqual(str(comment), expected_str)