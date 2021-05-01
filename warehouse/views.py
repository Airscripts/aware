from django.http import HttpResponse
from django.template import loader

from .models import Car, Filter

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, id):
    try:
        car = Car.objects.get(pk=id)
        filters = car.filters.all()

        template = loader.get_template('cars/detail.html')
        context = {
            'car': car,
            'filters': filters,
        }
    except Car.DoesNotExist:
        car = None
    return HttpResponse(template.render(context, request))