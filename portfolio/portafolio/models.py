from django.db import models
from django.db.models.fields import CharField,DateField,URLField
from django.db.models.fields.files import ImageField
from datetime import date

# Create your models here.

class Project(models.Model):
    title=CharField((""), max_length=50)
    description=CharField(max_length=50)
    image=ImageField((""), upload_to="portafolio/images", height_field=None, width_field=None, max_length=None)
    url=URLField(blank=True, max_length=200)
    date=DateField(default=date.today, auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.title
