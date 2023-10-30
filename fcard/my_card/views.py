from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import FlashWord
from .forms import *

# Create your views here.


#FleshWorddagi barcha wordlarni chiqazib olamiz

def index(request):
    #index sahifasiga biror metod yordamida o'tilgan bo'lsa
    if request.method == 'POST':
        form = FlashWordForm(request.POST)
        if form.is_valid():
            # agar word kiritilgan bo'lsa umumiy lug'atga qo'shadi
            # word = request.POST.get('word')
            # translate = request.POST.get('translate')
            # defenition = request.POST.get('defenition')
            # new_one = FlashWord(word=word, translate=translate, defenition=defenition)
            # new_one.save()
            #yuqoridagi 4 qator kodni bir qatorga kiritdi
            """birinchi html bilan, keyin Django.form yordamida forma yasadik.
            modellar uchun formalarni birinchisida qo'lda yozib , keyin modelfrom 
            yordamida mavjud modellarning formalarini avtomatik yaratdik"""

            band = form.save()

            #return redirect('wordpage', band.id)
            #word templatega qaytishimiz mumkun agar # ni olib qo'ysak

            # if the form is not valid, we let execution continue to the return
    else:
        # this must be a GET request, so create an empty form
        form = FlashWordForm()


    my_words = FlashWord.objects.all().order_by('word')
    context = {'my_words':my_words}

    return render(request, 'my_card/index.html', context=context)


def wordpage(request, smth):
    someword = FlashWord.objects.get(id=smth)
    return render(request, "my_card/word.html", {"someword":someword})

def add(request):
    #context = {'word':word, 'translate':translate, 'defenition':defenition}
    add_form = FlashWordForm()
    return render(request, "my_card/add.html", {'add_form':add_form})

def delete(request, id):
    someword = FlashWord.objects.get(id=id) # we need this for both GET and POST

    if request.method == 'POST':
        someword.delete()

        # redirect to the wordpage
        return redirect('index')
    # no need for an `else` here. If it's a GET request, just continue

    return render(request, "my_card/delete.html", {"someword": someword})

def update(request, id):
    someword = FlashWord.objects.get(id=id)
    form=FlashWordForm(instance=someword)
    if request.method == "POST":
        form = FlashWordForm(request.POST,  instance=someword) # prepopulate the form with an existing band
        if form.is_valid():
            #update the existing word
            form.save()
            return redirect('wordpage', someword.id)
        else:
            form = FlashWordForm(instance=someword)

    return render(request, "my_card/update.html", {"form": form})

#for testing
def testing(request):
  template = loader.get_template('my_card/template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))

