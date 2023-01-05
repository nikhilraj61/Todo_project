from django.db import models
from django.utils import timezone

# Create your models here.
class task(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    priority=models.IntegerField()
    email=models.EmailField(max_length=500)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
       return self.name

    # demo
    # description = models.TextField(max_length=220, blank=True, default=None)
    # image = models.ImageField(upload_to="/products_images/", null=True, blank=True, width_field="width_field",
    #                           height_field="height_field")
    # width_field = models.IntegerField(default=0)
    # height_field = models.IntegerField(default=0)
    # is_active = models.BooleanField(default=True)
    # publish = models.DateField(auto_now=False, auto_now_add=True)
    # timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
