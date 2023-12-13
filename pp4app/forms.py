from .models import Comment
from django import forms

from django import forms
from .models import Comment

class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)