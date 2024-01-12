from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Review, Ingredient, Utensil, Comment
from django import forms
from .forms import ReviewForm, CommentForms, CustomSignupForm, CustomLoginForm
from django.core.validators import RegexValidator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from allauth.account.views import SignupView
import requests
import os


def Homepage(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def bad_request(request, exception=None):
    print(f"Request to /400/ - User: {request.user}")
    return render(request, '400.html', status=400)


def permission_denied(request, exception=None):
    print(f"Request to /403/ - User: {request.user}")
    return render(request, '403.html', status=403)


def page_not_found(request, *args, **kwargs):
    return render(request, '404.html', status=404)


def server_error(request, exception=None):
    print(f"Request to /500/ - User: {request.user}")
    return render(request, '500.html', status=500)


class CustomSignupView(SignupView):
    template_name = 'account/signup.html'
    form_class = CustomSignupForm


class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = CustomLoginForm


class SearchForm(forms.Form):
    query = forms.CharField(
        validators=[
            RegexValidator(
                regex="^[a-zA-Z, ]+$",
                message="Only letters, commas, and spaces are allowed."
            )]
    )


def search(request):
    recipes = []
    query = ''

    if request.method == 'POST' or request.method == 'GET':
        form = SearchForm(request.POST or request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            recipes = get_recipes(query)

            paginator = Paginator(recipes, 16)
            page = request.GET.get('page', 1)
            try:
                recipes = paginator.page(page)
            except (PageNotAnInteger, EmptyPage):
                recipes = paginator.page(1)

    return render(request, 'search.html', {
        'form': form,
        'query': query,
        'recipes': recipes})


def get_recipes(query):
    api_url = 'https://api.edamam.com/api/recipes/v2'
    app_id = os.environ.get("EDA_APP_ID")
    app_key = os.environ.get("EDA_APP_KEY")

    params = {
        'q': query,
        'app_id': app_id,
        'app_key': app_key,
        'type': 'public'
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('hits', [])
    else:
        return []


def SubmitReview(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReviewForm(request.POST, request.FILES)
            if form.is_valid():
                review = form.save(commit=False)
                review.author = request.user
                review.save()
                form.save_m2m()

                existing_ingredients = form.cleaned_data.get('ingredients')
                review.ingredients.set(existing_ingredients)

                new_ingredient_string = form.cleaned_data.get(
                    'new_ingredient', '')
                new_ingredient_list = [
                    ingredient.strip()
                    for ingredient in new_ingredient_string.split(',')]

                for new_ingredient_name in new_ingredient_list:
                    try:
                        new_ingredient,
                        created = Ingredient.objects.get_or_create(
                            name=new_ingredient_name)
                        review.ingredients.add(new_ingredient)
                    except IntegrityError:
                        try:
                            new_ingredient = Ingredient.objects.get(
                                    name=new_ingredient_name)
                        except Ingredient.DoesNotExist:
                            new_ingredient_id = Ingredient.objects.latest(
                                    'id').id + 1
                            new_ingredient = Ingredient.objects.create(
                                id=new_ingredient_id, name=new_ingredient_name)
                        review.ingredients.add(new_ingredient)

                if review.featured_image_a:
                    print(f"Cloudinary URL: {review.featured_image_a.url}")
                else:
                    print("No Cloudinary URL (featured_image_a is None)")

                url = form.cleaned_data.get("url")
                if url:
                    request.session["modalURL"] = url
                    print(f"Session modalURL set to: {url}")

                messages.success(request, 'Review submitted successfully')

                return redirect('review_blog')
            else:
                print(form.errors)
        else:
            form = ReviewForm()
            print(form.errors)

        return render(request, 'submit_review.html', {
            'form': form,
            'ingredients': Ingredient.objects.all(),
            'utensils': Utensil.objects.all()})

    else:
        return redirect('login')


class Reviews(generic.ListView):
    model = Review
    template_name = 'review_blog.html'
    paginate_by = 8

    def get_queryset(self):
        sort_option = self.request.GET.get('sort', '-created_on')

        if sort_option == 'total_votes':
            queryset = Review.objects.filter(
                status=1).annotate(
                    net_votes_count=Count(
                        'up_vote') - Count(
                            'down_vote')).order_by(
                                '-net_votes_count',
                                '-created_on')
        else:
            queryset = Review.objects.filter(status=1).order_by('-created_on')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', '')
        return context


class ReviewPost(DetailView):
    model = Review
    template_name = 'review.html'
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            'comments'] = self.object.comments_review.filter(
                approved=True).order_by('created_on')
        print("Comments:", context['comments'])
        context['comment_form'] = CommentForms()
        context['commented'] = False
        context['ingredients'] = self.object.ingredients.all()
        context['utensils'] = self.object.utensils.all()

        liked = False
        disliked = False
        if self.object.up_vote.filter(id=self.request.user.id).exists():
            liked = True
        elif self.object.down_vote.filter(id=self.request.user.id).exists():
            disliked = True

        context['liked'] = liked
        context['disliked'] = disliked
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()

        comment_form = CommentForms(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.email = request.user.email
            comment.name = request.user.username
            comment.user = request.user
            comment.review = self.object
            comment.save()
            context['commented'] = True
            context['comment_form'] = CommentForms()
        else:
            print("Invalid comment form:", comment_form.errors)
            context['comment_form'] = comment_form

        return self.render_to_response(context)


class ReviewUpvote(View):
    def post(self, request, slug):
        review = get_object_or_404(Review, slug=slug)

        vote_type = request.POST.get('vote_type', None)
        if vote_type == 'upvote':
            messages.success(request, 'You have upvoted')
            review.up_vote.filter(id=request.user.id).exists() is False \
                and review.up_vote.add(request.user)
            review.down_vote.filter(id=request.user.id).exists() \
                and review.down_vote.remove(request.user)

        elif vote_type == 'downvote':
            messages.success(request, 'You have downvoted')
            review.down_vote.filter(id=request.user.id).exists() \
                is False and review.down_vote.add(request.user)
            review.up_vote.filter(id=request.user.id).exists() \
                and review.up_vote.remove(request.user)

        generated_url = reverse('review_post', args=[slug])

        return redirect(generated_url)


@method_decorator(login_required, name='dispatch')
class UpdateReview(View):
    template_name = 'update_review.html'

    def get(self, request, slug):
        review = get_object_or_404(Review, slug=slug, author=request.user)
        form = ReviewForm(instance=review)
        return render(
            request,
            self.template_name,
            {'form': form, 'review': review})

    def post(self, request, slug):
        review = get_object_or_404(Review, slug=slug, author=request.user)
        form = ReviewForm(request.POST, request.FILES, instance=review)

        if 'delete' in request.POST:
            review.delete()
            return redirect('blog')

        if form.is_valid():

            updated_review = form.save(commit=False)
            updated_review.author = request.user

            existing_ingredients = form.cleaned_data.get('ingredients')
            review.ingredients.set(existing_ingredients)

            existing_utensils = form.cleaned_data.get('utensils')
            review.utensils.set(existing_utensils)

            new_ingredient_string = form.cleaned_data.get('new_ingredient', '')
            new_ingredient_list = [
                ingredient.strip() for \
                    ingredient in new_ingredient_string.split(',')]

            for new_ingredient_name in new_ingredient_list:
                try:
                    new_ingredient, created = Ingredient.objects.get_or_create(
                        name=new_ingredient_name)
                    review.ingredients.add(new_ingredient)
                except IntegrityError:
                    try:
                        new_ingredient = Ingredient.objects.get(
                                name=new_ingredient_name)
                    except Ingredient.DoesNotExist:
                        new_ingredient_id = Ingredient.objects.latest(
                                'id').id + 1
                        new_ingredient = Ingredient.objects.create(
                            id=new_ingredient_id, name=new_ingredient_name)
                    review.ingredients.add(new_ingredient)

            updated_review.save()

            return redirect(reverse('blog'))

        return render(
            request,
            self.template_name,
            {'form': form, 'review': review})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST' and request.user.username == comment.name:
        comment.delete()
        messages.success(request, 'Comment deleted successfully')

    return redirect('review_post', slug=comment.review.slug)
