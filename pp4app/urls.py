from . import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage, name='home'),
    path('search/', views.Search, name='search'),
    path('blog/', views.Reviews.as_view(), name="blog"),
    path('<slug:slug>/', views.ReviewPost.as_view(), name='review_post'),
]