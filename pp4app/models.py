from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField

STATUS = ((0, "DRAFT"), (1, "Published"))

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    image_url = models.URLField()

    def __str__(self):
        return self.title

class Review(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField("image", default="placeholder")
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    upvotes = models.ManyToManyField(User, related_name="review_likes", blank=True)
    rating = models.ManyToManyField(User, related_name="review_rating", blank=True)
    prep_time = models.IntegerField(help_text='Preparation time in minutes')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.upvotes.count()

class Comment(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.text} by {self.name}"
