# Importing: Dependencies.
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Declaring: Choices.

CYLINDERS_CHOICES = [
  ('900', '900'),
  ('1000', '1000'),
  ('1200', '1200'),
  ('1300', '1300'),
  ('1500', '1500'),
  ('1600', '1600'),
  ('2000', '2000'),
]

# Declaring: Models.

# Declaring Filter Model.
class Filter(models.Model): 
  id = models.AutoField(primary_key=True)
  code = models.CharField(max_length=16, verbose_name="Codice")
  typology = models.CharField(max_length=32, verbose_name="Tipologia", choices=[('air', 'Aria'), ('oil', 'Olio'), ('passenger', 'Abitacolo'), ('diesel', 'Gasolio'), ('gas', 'Gas')])
  quantity = models.PositiveIntegerField(default=0, verbose_name="Quantita'")
  cars = models.ManyToManyField("Car", through="CarFilter", verbose_name="Auto")

  def __str__(self):
    # pylint: disable=E1101
    return self.code + " " + self.get_typology_display()
  
  class Meta:
    verbose_name = _("Filtro")
    verbose_name_plural = _("Filtri")

# Declaring Car Model.
class Car(models.Model):
  id = models.AutoField(primary_key=True)
  make = models.CharField(max_length=100, verbose_name="Produttore")
  model = models.CharField(max_length=100, verbose_name="Modello")
  year = models.CharField(max_length=4, verbose_name="Anno")
  engine = models.CharField(max_length=10, choices=[('petrol', 'Benzina'), ('diesel', 'Diesel')], default="petrol", verbose_name="Motore")
  cylinders = models.CharField(choices=CYLINDERS_CHOICES, verbose_name="Cilindrata", max_length=16)
  filters = models.ManyToManyField("Filter", through="CarFilter" , verbose_name="Filtri")

  def __str__(self):
    # pylint: disable=E1101
    return self.make + " " + self.model + " (" + self.get_engine_display() + ", " + self.year + ")" 

  class Meta:
    verbose_name = _("Auto")
    verbose_name_plural = _("Auto")
    unique_together = ("make", "model", "engine")

class CarFilter(models.Model):
  car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Auto")
  filter = models.ForeignKey(Filter, on_delete=models.CASCADE, verbose_name="Filtro")