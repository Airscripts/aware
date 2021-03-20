# Importing: Dependencies.
from django.contrib import admin

# Importing: Models.
from .models import Car
from .models import Filter

# Admin Class for Model Car.
class CarAdmin(admin.ModelAdmin):
    list_display = ('make','model','year', 'engine')
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
