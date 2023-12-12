from . import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage, name='home'),
    path('search/', views.search, name='search'),
    path('submit_review/', views.SubmitReview, name='submit_review'),
    path('blog/', views.Reviews.as_view(), name="blog"),
    path('<slug:slug>/', views.ReviewPost.as_view(), name='review_post'),
]