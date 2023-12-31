from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Review, Ingredient, Utensil
from .forms import CommentForms, ReviewForm
import requests
import os

def Homepage(request):
    return render(request, 'index.html')

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def About(request):
        return render(request, 'about.html')

def search(request):
    recipes = []

    if request.method == 'POST':
        query = request.POST.get('query')
        recipes = get_recipes(query)

    elif request.method == 'GET':
        query = request.GET.get('query')
        page = request.GET.get('page', 1)

        if query:
            recipes = get_recipes(query)

            paginator = Paginator(recipes, 16)
            try:
                recipes = paginator.page(page)
            except PageNotAnInteger:
                recipes = paginator.page(1)
            except EmptyPage:
                recipes = paginator.page(paginator.num_pages)

    return render(request, 'search.html', {'query': query, 'recipes': recipes})

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
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            form.save_m2m()

            existing_ingredients = form.cleaned_data.get('ingredients')
            review.ingredients.set(existing_ingredients)

            new_ingredient_string = form.cleaned_data.get('new_ingredient', '')
            new_ingredient_list = [ingredient.strip() for ingredient in new_ingredient_string.split(',')]

            for new_ingredient_name in new_ingredient_list:
                try:
                    new_ingredient, created = Ingredient.objects.get_or_create(name=new_ingredient_name)
                    review.ingredients.add(new_ingredient)
                except IntegrityError:
                    try:
                        new_ingredient = Ingredient.objects.get(name=new_ingredient_name)
                    except Ingredient.DoesNotExist:
                        new_ingredient_id = Ingredient.objects.latest('id').id + 1
                        new_ingredient = Ingredient.objects.create(id=new_ingredient_id, name=new_ingredient_name)
                    review.ingredients.add(new_ingredient)

            if review.featured_image:
                print(f"Cloudinary URL: {review.featured_image.url}")
            else:
                print("No Cloudinary URL available (featured_image is None)")

            url = form.cleaned_data.get("url")
            if url:
                request.session["modalURL"] = url
                print(f"Session modalURL set to: {url}")

            return redirect('review_blog')
        else:
            print(form.errors)
    
    else:
        
        form = ReviewForm()
        print(form.errors)

    return render(request, 'submit_review.html', {'form': form, 'ingredients': Ingredient.objects.all(), 'utensils': Utensil.objects.all()})

class Reviews(generic.ListView):
    model = Review
    template_name = 'review_blog.html'
    paginate_by = 8

    def get_queryset(self):
        sort_option = self.request.GET.get('sort', '-created_on')
        print(f"Sort option: {sort_option}")

        if sort_option == 'upvotes':
            queryset = Review.objects.filter(status=1).annotate(net_votes_count=Count('upvotes') - Count('downvotes')).order_by('-net_votes_count', '-created_on')
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
        context['comments'] = self.object.comments_review.filter(approved=True).order_by('created_on')
        print("Comments:", context['comments'])
        context['comment_form'] = CommentForms()
        context['commented'] = False
        context['ingredients'] = self.object.ingredients.all()
        context['utensils'] = self.object.utensils.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()

        comment_form = CommentForms(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.review = self.object
            comment.save()
            context['commented'] = True
            context['comment_form'] = CommentForms()
        else:
            context['comment_form'] = comment_form

        return self.render_to_response(context)
    
class ReviewUpvote(View):
    template_name = 'review.html'

    def post(self, request, *args, **kwargs):
        review = get_object_or_404(Review, slug=self.kwargs['slug'])

        # Initialize the variables with default values
        user_has_upvoted = False
        user_has_downvoted = False

        if request.user.is_authenticated:
            upvote_value = int(request.POST.get('upvote', 0))

            if upvote_value == 1:
                user_has_upvoted = review.upvotes.filter(id=request.user.id).exists()
                if user_has_upvoted:
                    # Remove upvote
                    review.upvotes.remove(request.user)
                else:
                    # Add upvote and remove potential downvote
                    review.upvotes.add(request.user)
                    review.downvotes.remove(request.user)  # Remove potential downvote
                    # User has clicked upvote, so set downvote status accordingly
                    user_has_downvoted = False
            elif upvote_value == 0:
                user_has_downvoted = review.downvotes.filter(id=request.user.id).exists()
                if user_has_downvoted:
                    # Remove downvote
                    review.downvotes.remove(request.user)
                else:
                    # Add downvote and remove potential upvote
                    review.downvotes.add(request.user)
                    review.upvotes.remove(request.user)  # Remove potential upvote
                    # User has clicked downvote, so set upvote status accordingly
                    user_has_upvoted = False

        # Calculate net votes
        net_votes = review.upvotes.count() - review.downvotes.count()
        print(f"Net votes: {net_votes}")

        # Pass user voting status and net votes to the template
        context = {
            'review': review,
            'user_has_upvoted': user_has_upvoted,
            'user_has_downvoted': user_has_downvoted,
            'net_votes': net_votes,
        }

        return render(request, self.template_name, context)
    
@method_decorator(login_required, name='dispatch')
class UpdateReview(View):
    template_name = 'update_review.html'

    def get(self, request, slug):
        review = get_object_or_404(Review, slug=slug, author=request.user)
        form = ReviewForm(instance=review)
        return render(request, self.template_name, {'form': form, 'review': review})

    def post(self, request, slug):
        review = get_object_or_404(Review, slug=slug, author=request.user)
        form = ReviewForm(request.POST, instance=review)

        if 'delete' in request.POST:
            review.delete()
            return redirect('blog')
        
        if form.is_valid():
            if form.is_valid():
                review = form.save(commit=False)

                review.ingredients.clear()

                existing_ingredients = form.cleaned_data.get('ingredients')
                review.ingredients.set(existing_ingredients)

                new_ingredient_string = form.cleaned_data.get('new_ingredient', '')
                new_ingredient_list = [ingredient.strip() for ingredient in new_ingredient_string.split(',')]

                for new_ingredient_name in new_ingredient_list:
                    try:
                        new_ingredient, created = Ingredient.objects.get_or_create(name=new_ingredient_name)
                        review.ingredients.add(new_ingredient)
                    except IntegrityError:
                        try:
                            new_ingredient = Ingredient.objects.get(name=new_ingredient_name)
                        except Ingredient.DoesNotExist:
                            new_ingredient_id = Ingredient.objects.latest('id').id + 1
                            new_ingredient = Ingredient.objects.create(id=new_ingredient_id, name=new_ingredient_name)
                        review.ingredients.add(new_ingredient)
                form.save()
                return redirect(review.get_absolute_url())
        
        return render(request, self.template_name, {'form': form, 'review': review})