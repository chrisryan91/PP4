from django import forms
from .models import Review, Comment, Ingredient, Utensil
from cloudinary.forms import CloudinaryFileField
from django.utils.text import slugify

class ReviewForm(forms.ModelForm):
    featured_image = CloudinaryFileField(required=False)
    new_ingredient = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Review
        fields = ['title', 'recipe', 'content', 'featured_image', 'prep_time', 'url', 'ingredients', 'utensils']
        
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['recipe'].widget.attrs['readonly'] = True
        self.fields['url'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()
        featured_image = cleaned_data.get('featured_image')

        if not featured_image:
            raise forms.ValidationError('You must upload an image to Cloudinary.')

        return cleaned_data

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
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)