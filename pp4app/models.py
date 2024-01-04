from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django.urls import reverse
from cloudinary.models import CloudinaryField

STATUS = ((0, "DRAFT"), (1, "Published"))

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Utensil(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CuisineType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Review(models.Model):       
    VOTE_CHOICES = (
        (0, 'Not Voted Yet'),
        (1, 'Upvote'),
        (2, 'Downvote'),
    )
        
    title = models.CharField(max_length=100, unique=True)
    recipe = models.CharField(max_length=100, unique=False, default="default")
    url = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    # new_ingredient = models.CharField(max_length=100)
    utensils = models.ManyToManyField(Utensil, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image_a = CloudinaryField("image", default="placeholder")
    featured_image_b = models.URLField(blank=True, null=True, max_length=5000)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    cuisine_type = models.ManyToManyField(CuisineType, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    prep_time = models.PositiveIntegerField(help_text='Preparation time in minutes', blank=True, null=True)
    up_vote = models.ManyToManyField(User, related_name='news_up_vote', blank=True)
    down_vote = models.ManyToManyField(User, related_name='news_down_vote', blank=True)

    class Meta:   
        ordering = ['-created_on']

    def number_of_up_votes(self):
        return self.up_vote.count()

    def number_of_down_votes(self):
        return self.down_vote.count()
    
    def total_votes(self):
        return self.up_vote.count() - self.down_vote.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('review_post', kwargs={'slug': self.slug})
    
    
class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments_review")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
