from django.db import models


# Create your models here.


class Images(models.Model):
    # username = models.CharField(max_length=250, unique=True)
    # password = models.CharField(max_length=250)
    # title = models.CharField(max_length=150)
    # body = models.TextField()
    # tags = models.CharField(max_length=150)
    # date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.username

# class Meta:
#     db_table = "my_user_table"


class EmailForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)


class Service(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name


class CrossfitTraining(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='image')
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
