from django.db import models

# Create your models here.



    

class Posts(models.Model):
    
    title = models.CharField("Название блюда", max_length=50)
    price = models.IntegerField("Цена блюда")
    description = models.TextField("Описание", max_length=300)
    compound = models.CharField("Состав", max_length=300)
    #img = models.ImageField(
        #"Изображение", upload_to="main/static/main/img", default="Не удалось получить картинку")
    elements=(
        ("Холодные роллы","Холодные роллы"),
        ("Напитки","Напитки"),
        ("Горячие роллы","Горячие роллы"),
        ("Запеченные роллы","Запеченные роллы"),
        ("Десерты","Десерты"),
        ("Горячие блюда","Горячие блюда"),
        ("Салаты","Салаты"),
        ("Супы","Супы"),
        
        
        
        
        )
    category=models.CharField("Категория",max_length=100,choices=elements)
    
    

    def __str__(self):
        return self.title

