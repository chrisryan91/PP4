from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Review

def Homepage(request):
    return render(request, 'index.html')

def Search(request):
    return render(request, 'search.html')

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