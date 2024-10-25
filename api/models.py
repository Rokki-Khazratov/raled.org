from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    url = models.URLField()
    thumb = models.ImageField(upload_to='thumbs/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    univercity_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.univercity_name


class About(models.Model):
    address = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=1000)

    def __str__(self):
        return self.address
    
class History(models.Model):
    name = models.TextField()

    def __str__(self):
        return "History"



class Social_media(models.Model):
    icon = models.CharField(max_length=50)
    url = models.URLField()



class News(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField(blank=True,null=True)
    thumb = models.ImageField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class Member(models.Model):
    name= models.CharField(max_length=255)
    work_place = models.TextField()
    discription = models.TextField(blank=True,null=True)
    img = models.ImageField(upload_to='members/',blank=True,null=True)


    def __str__(self):
        return self.name
    

class BookOrder(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    book_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order: {self.book_name} by {self.name} at {self.created_at}"