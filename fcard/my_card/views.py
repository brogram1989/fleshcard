from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import FlashWord

# Create your views here.


#FleshWorddagi barcha wordlarni chiqazib olamiz

def index(request):
    word = FlashWord.objects.all().values()
    context = {'word':word, }
    return render(request, 'my_card/index.html', context=context)








