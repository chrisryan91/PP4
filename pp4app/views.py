from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Review
from decouple import config
import requests
import os

def Homepage(request):
    return render(request, 'index.html')

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

            paginator = Paginator(recipes, 8)
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
    return render(request, 'submit_review.html')

class Reviews(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'review_blog.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.queryset
        return context

class ReviewPost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "review.html",
            {
            "review": review,
            }
        )