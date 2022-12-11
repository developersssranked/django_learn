from django.db import models

# Create your models here.


class reviews(models.Model):
    title = models.CharField("Заголовок отзыва", max_length=50)

    reviews_text = models.TextField("Текст отзыва")

    username = models.CharField("Имя пользователя", max_length=100)
    score = models.IntegerField("Оценка пользователя")
