from .models import Review, Comment
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'prep_time']
class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'review']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)