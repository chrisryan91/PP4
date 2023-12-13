from .models import Comment
from django import forms

class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'review']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)