from django.shortcuts import render
from .models import Posts

# Create your views here.


def menu_home(request):
    menus = Posts.objects.all()
    
    return render(request, 'menu/menu_home.html', {"menus": menus})
def cook_rolls(request):
    menus = Posts.objects.all()
    
    return render(request, 'menu/cook_rolls.html', {"menus": menus})
def cold_rolls(request):
    menus = Posts.objects.all()
    
    return render(request, 'menu/cold_rolls.html', {"menus": menus})
def hot_rolls(request):
    menus = Posts.objects.all()
    
    return render(request, 'menu/hot_rolls.html', {"menus": menus})
def desserts(request):
    menus = Posts.objects.all()
    
    return render(request, 'menu/desserts.html', {"menus": menus})
def hot_dishes(request):
    menus = Posts.objects.all()
    
    return render(request, 'menu/hot_dishes.html', {"menus": menus})
def salads(request):
    menus = Posts.objects.all()
    
    return render(request, 'menu/salads.html', {"menus": menus})
def soups(request):
    menus = Posts.objects.all()
    
    return render(request, 'menu/soups.html', {"menus": menus})
def drinks(request):
    menus = Posts.objects.all()
    
    return render(request, 'menu/drinks.html', {"menus": menus})