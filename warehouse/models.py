# Importing: Dependencies.
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Declaring: Models.

# Declaring Car Model.
class Car(models.Model):
  make = models.CharField(max_length=100, verbose_name="Produttore")
  model = models.CharField(max_length=100, verbose_name="Modello")
  year = models.CharField(max_length=4, verbose_name="Anno")
  engine = models.CharField(max_length=10, choices=[('petrol', 'Benzina'), ('diesel', 'Diesel')], default="petrol", verbose_name="Motore")

  def __str__(self):
    # pylint: disable=E1101
    return self.make + " " + self.model + " (" + self.get_engine_display() + ", " + self.year + ")" 

  class Meta:
    verbose_name = _("Auto")
    verbose_name_plural = _("Auto")
    unique_together = ("make", "model", "engine")

# Declaring Filter Model.
class Filter(models.Model): 
  code = models.CharField(max_length=16, verbose_name="Codice")
  typology = models.CharField(max_length=100, verbose_name="Tipologia")
  quantity = models.PositiveIntegerField(default=0, verbose_name="Quantita'")
  car = models.ForeignKey(Car, verbose_name="Auto", on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
   return 'Filtro: ' + self.code + " " + self.typology
  
  class Meta:
    verbose_name = _("Filtro")
    verbose_name_plural = _("Filtri")
