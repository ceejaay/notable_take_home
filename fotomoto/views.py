from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Images

def index(request):
    image_list = Images.objects.all()
    template = loader.get_template('index.html')
    context = {
            'all_images': image_list
            }
    return HttpResponse(template.render({'pics': image_list }, request))

# Create your views here
