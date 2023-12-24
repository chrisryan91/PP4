from . import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage, name='home'),
    path('search/', views.search, name='search'),
    path('submit_review/', views.SubmitReview, name='submit_review'),
    path('blog/', views.Reviews.as_view(), name="blog"),
    path('<slug:slug>/', views.ReviewPost.as_view(), name='review_post'),
    path('review_blog.html', views.Reviews.as_view(), name='review_blog'),
    path('upvotes/<slug:slug>', views.ReviewUpvote.as_view(), name="review_upvote"),
    path('update_review/<slug:slug>/', views.UpdateReview.as_view(), name='update_review'),
    path('review/<slug:slug>/', views.ReviewPost.as_view(), name='review_post'),
    path('blog/', views.Reviews.as_view(), name='reviews'),
]