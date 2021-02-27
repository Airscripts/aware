# Importing: Dependencies.
from django.contrib import admin

# Importing: Models.
from .models import Car

# Registering models.
admin.site.register(Car)

# Overriding text.
admin.site.site_header = "Morazyne"
admin.site.index_title = "Dashboard"
admin.site.site_title = "Morazyne"
