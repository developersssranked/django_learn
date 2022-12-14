# Generated by Django 4.1.4 on 2022-12-11 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок отзыва')),
                ('reviews_text', models.TextField(verbose_name='Текст отзыва')),
                ('username', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('score', models.IntegerField(verbose_name='Оценка пользователя')),
            ],
        ),
    ]
