from django.test import TestCase
from ..models import Review, Ingredient, Utensil, Comment
from django.utils.text import slugify
from django.contrib.auth.models import User


class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='mark',
            password='patterson'
        )
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

    def test_review_creation(self):
        self.assertEqual(self.review.title, 'Delicious Stir Fry')
        self.assertEqual(self.review.recipe, 'Stir Fry')
        self.assertEqual(self.review.author, self.user)
        self.assertEqual(self.review.content, '... blah blah blah...')
        self.assertEqual(self.review.prep_time, 10)
        self.assertTrue(self.review.status in dict(Review._meta.get_field('status').choices).keys())

    def test_review_upvote(self):
        second_user = User.objects.create_user(
            username='MarkP',
            password='malahide'
        )
        self.review.up_vote.add(self.user)
        self.review.up_vote.add(second_user)

        self.assertEqual(self.review.number_of_up_votes(), 2)

    def test_review_downvote(self):
        second_user = User.objects.create_user(
            username='RichieL',
            password='compton'
        )
        self.review.down_vote.add(self.user)
        self.review.down_vote.add(second_user)

        self.assertEqual(self.review.number_of_down_votes(), 2)

    def test_review_total_votes(self):
        second_user = User.objects.create_user(
            username='testuser2',
            password='testpassword'
        )
        self.review.up_vote.add(self.user)
        self.review.down_vote.add(second_user)

        self.assertEqual(self.review.total_votes(), 0)

    def test_comment_creation(self):
        comment = Comment.objects.create(
            review=self.review,
            name='Test Commenter',
            email='test@example.com',
            body='Test Comment Body'
        )

        self.assertEqual(comment.review, self.review)
        self.assertEqual(comment.name, 'Test Commenter')
        self.assertEqual(comment.email, 'test@example.com')
        self.assertEqual(comment.body, 'Test Comment Body')
