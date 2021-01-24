from django.db import models
from django.contrib.auth.models import User

ORG = (
    ("fundation", "Fundacja"),
    ("organization", "Organizacja pozarządowa"),
    ("local", "Zbiórka lokalna"),
)


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=64, choices=ORG)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=8)
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # class User:
    # username
    # first_name
    # last_name
    # email
    # password
    # groups
    # user_permissions
    # is_staff
    # is_active
    # is_superuser
    # last_login
    # date_joined
