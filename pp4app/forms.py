from .models import Review, Comment
from cloudinary.forms import CloudinaryFileField
from django import forms
from django.utils.text import slugify

class ReviewForm(forms.ModelForm):
    featured_image = CloudinaryFileField(required=False)

    class Meta:
        model = Review
        fields = ['title', 
                'content', 
                'featured_image', 
                'prep_time',
                'url', 
                'ingredients', 
                'utensils']
        widgets = {
                'ingredients': forms.Textarea(attrs={'rows': 3}),
                'utensils': forms.Textarea(attrs={'rows': 3}),
                }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)

        if isinstance(instance.featured_image, str):
            instance.featured_image = CloudinaryFileField("image").to_python(instance.featured_image)

        if commit:
            instance.save()
        return instance
    
class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'review']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)