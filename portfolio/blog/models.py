from django.db import models
from datetime import date
# Create your models here.

class Post(models.Model):
    title=models.CharField((""), max_length=50)
    description=models.CharField(max_length=50)
    image=models.ImageField((""), upload_to="portafolio/images", height_field=None, width_field=None, max_length=None)
    date=models.DateField(default=date.today, auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.title