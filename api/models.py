from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    LANGUAGE_CHOICES = [
        ('uz', 'Uzbek'),
        ('ru', 'Russian'),
        ('en', 'English'),
        #nechta til sorash!
    ]

    name = models.CharField(max_length=250)
    description = models.TextField()
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='uz')
    url = models.URLField()
    thumb = models.ImageField(upload_to='thumbs/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
