from .models import Review, Comment
from django import forms
from django.utils.text import slugify

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'prep_time']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance
    
class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'review']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)