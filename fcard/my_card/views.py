from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import FlashWord

# Create your views here.


#FleshWorddagi barcha wordlarni chiqazib olamiz

def index(request):
    my_words = FlashWord.objects.all().values()

    #template = loader.get_template('my_card/index.html')
    #yuqoridagi ikkinchi variant view uchun, lekin natija bir xil bo'ladi
    context = {'my_words':my_words, }
    return render(request, 'my_card/index.html', context=context)
    #return HttpResponse(template.render(context, request))
    # yuqoridagi ikkinchi variant view uchun, lekin natija bir xil bo'ladi








