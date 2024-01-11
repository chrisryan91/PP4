from django import forms
from .models import Review, Comment, Ingredient, Utensil
from django.contrib.auth.forms import AuthenticationForm
from cloudinary.forms import CloudinaryFileField
from django.utils.text import slugify
from allauth.account.forms import SignupForm, LoginForm


class ReviewForm(forms.ModelForm):
    featured_image_a = CloudinaryFileField(required=False)
    new_ingredient = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Review
        fields = [
            'title',
            'recipe',
            'content',
            'cuisine_type',
            'new_ingredient',
            'featured_image_a',
            'prep_time',
            'url',
            'ingredients',
            'utensils']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['recipe'].widget.attrs['readonly'] = True
        self.fields['url'].widget.attrs['readonly'] = True

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        instance.author = user
        instance.slug = slugify(instance.title)

        if 'featured_image_a' in \
                self.cleaned_data and self.cleaned_data['featured_image_a']:
            instance.featured_image_a = self.cleaned_data['featured_image_a']
        else:
            instance.featured_image_a = None

        if commit:
            instance.save()

        return instance


class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CustomSignupForm(SignupForm):
    email = forms.EmailField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
