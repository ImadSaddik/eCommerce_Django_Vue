from django.urls import path
from review import views


urlpatterns = [
    path('reviews/<slug:product_slug>/', views.ReviewDetail.as_view()),
    path('sendReview/', views.sendReview),
]
