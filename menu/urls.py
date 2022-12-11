from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.menu_home, name="menu_home"),
    path('category=cook_rolls/', views.cook_rolls,name="cook-rolls"),
    path('category=cold_rolls/', views.cold_rolls,name="cold-rolls"),
    path('category=hot_rolls/', views.hot_rolls,name="hot-rolls"),
    path('category=hot_dishes/', views.hot_dishes,name="hot-dishes"),
    path('category=desserts/', views.desserts,name="desserts"),
    path('category=salads/', views.salads,name="salads"),
    path('category=drinks/', views.drinks,name="drinks"),
    path('category=soups/', views.soups,name="soups"),

]
