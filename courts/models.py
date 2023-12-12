from django.db import models
from courts.models import members

# Create your models here.
class Court(models.Model):
  courtname = models.CharField(max_length=255)
  #草地、硬地、泥地、地毯
  class Land(models.TextChoices):
    GRASS="1", "草地"
    HARD="2", "硬地"
    DIRT="3", "泥地"
    CARPET="4", "地毯"
  courtland = models.CharField(max_length=1, choices=Land.choices, default=1)
  courtcity = models.CharField(max_length=255, null=True)

  def __str__(self):
    return f"{self.courtname}, {self.courtland}, {self.courtcity}"