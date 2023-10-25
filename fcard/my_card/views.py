from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import FlashWord

# Create your views here.


#FleshWorddagi barcha wordlarni chiqazib olamiz

def index(request):

    wrd = request.POST.get('wrd')
    trnslt = request.POST.get('trnslt')
    dfntn = request.POST.get('dfntn')
    #agar wrd kiritilgan bo'lsa umumiy lug'atga qo'shadi
    if wrd :
        new_one = FlashWord(word=wrd, translate=trnslt, defenition=dfntn)
        new_one.save()
    else:
        pass

    my_words = FlashWord.objects.all()
    context = {'my_words':my_words}

    return render(request, 'my_card/index.html', context=context)


def wordpage(request, smth):
    someword = FlashWord.objects.get(word=smth)
    return render(request, "my_card/word.html", {"someword":someword})

def add(request):
    #context = {'word':word, 'translate':translate, 'defenition':defenition}
    return render(request, "my_card/add.html")

def delate(request):
    pass

def update(request, smth):
    someword = FlashWord.objects.get(word=smth)
    return render(request, "my_card/update.html", {"someword": someword})

#for testing
def testing(request):
  template = loader.get_template('my_card/template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))

