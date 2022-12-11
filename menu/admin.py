from django.contrib import admin

from .models import Posts

from reviews.models import reviews
admin.site.register(Posts)
admin.site.register(reviews)

