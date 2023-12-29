from django import forms
from .models import Review, Comment, Ingredient, Utensil
from cloudinary.forms import CloudinaryFileField
from django.utils.text import slugify

class ReviewForm(forms.ModelForm):
    featured_image = CloudinaryFileField(required=False)

    class Meta:
        model = Review
        fields = ['title', 'content', 'featured_image', 'prep_time', 'url', 'ingredients', 'utensils']
        
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['readonly'] = True
        self.fields['url'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)

        if isinstance(instance.featured_image, str):
            instance.featured_image = CloudinaryFileField("image").to_python(instance.featured_image)

        if commit:
            instance.save()
            self.save_m2m()

        return instance
    
class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)