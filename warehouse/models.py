# Importing: Dependencies.
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Declaring: Models.
class Car(models.Model):
  make = models.CharField(max_length=100, verbose_name="Produttore")
  model = models.CharField(max_length=100, verbose_name="Modello")
  year = models.CharField(max_length=4, verbose_name="Anno")
  engine = models.CharField(max_length=10, choices=[('petrol', 'Benzina'), ('diesel', 'Diesel')], default="petrol", verbose_name="Motore")

  def __str__(self):
   return 'Auto: ' + self.model

  class Meta:
    verbose_name = _("Auto")
    verbose_name_plural = _("Auto")
    unique_together = ("make", "model", "engine")