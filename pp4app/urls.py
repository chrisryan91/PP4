from . import views
from django.urls import path

urlpatterns = [
    path('', views.Reviews.as_view(), name="home"),
    path('<slug:slug>/', views.ReviewPost.as_view(), name='review_post'),
]