from django.db import models

# Create your models here.
class FoodType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

class FoodServing(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', blank=False, null=False)
    date = models.DateTimeField(auto_created=True, verbose_name='Date')
    price = models.IntegerField(verbose_name='Price', blank=False, null=False)
    picture = models.ImageField(verbose_name='Picture')
    description = models.TextField(verbose_name='Description')
    type = models.ForeignKey(FoodType, verbose_name='Type', on_delete=models.RESTRICT, null=True, blank=True)
