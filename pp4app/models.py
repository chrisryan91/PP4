from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from cloudinary.models import CloudinaryField

STATUS = ((0, "DRAFT"), (1, "Published"))

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Utensil(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Review(models.Model):
    title = models.CharField(max_length=100, unique=True)
    url = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    ingredients = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    utensils = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField("image", default="placeholder")
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    upvotes = models.ManyToManyField(User, related_name="review_likes", blank=True)
    prep_time = models.IntegerField(help_text='Preparation time in minutes')
    comments = models.ManyToManyField('pp4app.Comment', related_name='review_comments')
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.upvotes.count()
    
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