from . import views
from django.urls import path

urlpatterns = [
    path('search/', views.search, name='search'),
    path('about/', views.About, name='about'),
    path('submit_review/', views.SubmitReview, name='submit_review'),
    path('blog/', views.Reviews.as_view(), name="blog"),
    path('review_blog.html', views.Reviews.as_view(), name='review_blog'),
    path('upvotes/<slug:slug>/', views.ReviewUpvote.as_view(), name="review_upvote"),
    path('update_review/<slug:slug>/', views.UpdateReview.as_view(), name='update_review'),
    path('review/<slug:slug>/', views.ReviewPost.as_view(), name='review_post_detail'),
    path('blog/', views.Reviews.as_view(), name='reviews'),
    path('accounts/signup/', views.CustomSignupView.as_view(), name='signup'),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('<path:unmatched_path>/', views.page_not_found, name='custom_404_unmatched'),
    path('<slug:slug>/', views.ReviewPost.as_view(), name='review_post'),
    path('', views.Homepage, name='home'),
]


handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.server_error