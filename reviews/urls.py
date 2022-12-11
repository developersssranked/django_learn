from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.review, name="reviews"),
    path('create/', views.create_reviews, name="create")

]
