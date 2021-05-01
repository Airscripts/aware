# Importing: Dependencies.
from django import forms
from django.contrib import admin
from django.utils.html import format_html

# Importing: Models.
from .models import Car
from .models import Filter

# Admin Class for Model Car.
class CarAdmin(admin.ModelAdmin):
    def azioni(self, obj):
        print(obj.id)
        return format_html('<a class="btn" href="/cars/%s">Apri</a>' % obj.id, obj)

    list_display = ('make','model','year', 'engine', 'azioni')
    search_fields = ['model']

# Admin Class for Model Filter.
class FilterAdmin(admin.ModelAdmin):
    list_display = ('code', 'typology', 'quantity')
    search_fields = ['code']

# Registering models.
admin.site.register(Car, CarAdmin)
admin.site.register(Filter, FilterAdmin)

# Overriding text.
admin.site.site_header = "Morazyne"
admin.site.index_title = "Dashboard"
admin.site.site_title = "Morazyne"
