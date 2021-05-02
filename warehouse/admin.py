# Importing: Dependencies.
from django import forms
from django.contrib import admin
from django.utils.html import format_html

# Importing: Models.
from .models import Car
from .models import Filter

class FilterInline(admin.TabularInline):
    model = Car.filters.through
    verbose_name = 'Filtro Auto'
    verbose_name_plural = 'Filtri Auto'
    fields = ['filter', 'filter_typology', 'filter_quantity']
    readonly_fields = ['filter_typology', 'filter_quantity']
    extra = 0

    def filter_quantity(self, instance):
        return instance.filter.quantity

    def filter_typology(self, instance):
        return instance.filter.get_typology_display()

    filter_quantity.short_description = "Quantita'"
    filter_typology.short_description = "Tipologia"

class CarInline(admin.TabularInline):
    model = Filter.cars.through
    verbose_name = 'Auto con questo filtro'
    verbose_name_plural = 'Auto'
    fields = ['car', 'car_engine', 'car_year']
    readonly_fields = ['car_engine', 'car_year']
    extra = 0

    def car_year(self, instance):
        return instance.car.year

    def car_engine(self, instance):
        return instance.car.get_engine_display() 

    car_year.short_description = "Anno"
    car_engine.short_description = "Motore"

# Admin Class for Model Car.
class CarAdmin(admin.ModelAdmin):
    def azioni(self, obj):
        return format_html('<a class="btn" href="/warehouse/car/%s/change">Apri</a>' % obj.id, obj)

    list_display = ('make','model','year', 'engine', 'azioni')
    list_filter = ('make', 'year', 'engine')
    list_per_page = 10
    inlines = [FilterInline]
    search_fields = ['model']

# Admin Class for Model Filter.
class FilterAdmin(admin.ModelAdmin):
    def azioni(self, obj):
        return format_html('<a class="btn" href="/warehouse/filter/%s/change">Apri</a>' % obj.id, obj)

    list_display = ('code', 'typology', 'quantity', 'azioni')
    list_filter = ('typology', )
    list_per_page = 10
    search_fields = ['code']
    inlines = [CarInline]

# Registering models.
admin.site.register(Car, CarAdmin)
admin.site.register(Filter, FilterAdmin)

# Overriding text.
admin.site.site_header = "Morazyne"
admin.site.index_title = "Dashboard"
admin.site.site_title = "Morazyne"
