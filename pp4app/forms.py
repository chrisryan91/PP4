from django import forms
from .models import Review, Comment, Ingredient, Utensil
from cloudinary.forms import CloudinaryFileField
from django.utils.text import slugify

class ReviewForm(forms.ModelForm):
    featured_image = CloudinaryFileField(required=False)

    custom_utensil = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Add custom utensil'}),
        required=False
    )

    custom_ingredient = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Add custom ingredient'}),
        required=False
    )

    class Meta:
        model = Review
        fields = ['title', 'content', 'featured_image', 'prep_time', 'url', 'ingredients', 'utensils']
        
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['readonly'] = True
        self.fields['url'].widget.attrs['readonly'] = True

    def clean_custom_utensil(self):
        custom_utensil = self.cleaned_data['custom_utensil']
        if custom_utensil and Utensil.objects.filter(name=custom_utensil).exists():
            raise forms.ValidationError("This utensil already exists.")
        return custom_utensil

    def clean_custom_ingredient(self):
        custom_ingredient = self.cleaned_data['custom_ingredient']
        if custom_ingredient and Ingredient.objects.filter(name=custom_ingredient).exists():
            raise forms.ValidationError("This ingredient already exists.")
        return custom_ingredient

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)

        if isinstance(instance.featured_image, str):
            instance.featured_image = CloudinaryFileField("image").to_python(instance.featured_image)

        # Handle custom utensils and ingredients
        custom_utensil = self.cleaned_data['custom_utensil']
        custom_ingredient = self.cleaned_data['custom_ingredient']

        if custom_utensil:
            utensil, _ = Utensil.objects.get_or_create(name=custom_utensil)
            instance.utensils.add(utensil)

        if custom_ingredient:
            ingredient, _ = Ingredient.objects.get_or_create(name=custom_ingredient)
            instance.ingredients.add(ingredient)

        if commit:
            instance.save()

        return instance
    
class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)