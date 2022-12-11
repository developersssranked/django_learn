from django.shortcuts import render, redirect

from django.shortcuts import render
from .forms import reviewsForm
from .models import reviews
# Create your views here.


def review(request):
    reviewss = reviews.objects.all()
    return render(request, 'reviews/reviews_home.html', {"reviewss": reviewss})


def create_reviews(request):
    error = ""
    if request.method == 'POST':
        form = reviewsForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')

        else:
            error = "Форма заполнена некоректно"

    form = reviewsForm()
    data = {"form": form,
            "error": error}

    return render(request, 'reviews/create.html', data)
