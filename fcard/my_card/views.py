from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Word, Set
from .forms import *

# Create your views here.


#Set modeldagi barcha setlarni chiqazib olamiz

def index(request):
    my_sets = Set.objects.all()
    context = {'my_sets': my_sets }
    return render(request, 'my_card/index.html', context=context)

def set_create(request):

    if request.method == 'POST':
        form = SetForm(request.POST)
        if form.is_valid():
            # agar word kiritilgan bo'lsa umumiy lug'atga qo'shadi
            set = form.save()
            return redirect('index')
    else:
        # this must be a GET request, so create an empty form
        set_create = SetForm()

    return render(request, "my_card/set_create.html", {'set_create':set_create})
def set_list(request, id):
 
    my_set = Set.objects.get(id=id)
    context = {"my_set":my_set}
    return render(request, "my_card/set_list.html", context=context )

def set_update(request, id):
    someset = Set.objects.get(id=id)
    form = SetForm(instance=someset)
    if request.method == 'POST':
        form = SetForm(request.POST, instance=someset)# prepopulate the form with an existing band
        if form.is_valid():
            #update existing set
            form.save()
            return redirect('set_list', someset.id)
        else:
            form = SetForm(instance=someset)

    return render(request, "my_card/set_update.html", {"form": form})
def set_delete(request, id):
    someset = Set.objects.get(id=id)   # we need this for both GET and POST

    if request.method == 'POST':
        someset.delete()
        # redirect to the wordpage
        return redirect('index')
    # no need for an `else` here. If it's a GET request, just continue
    return render(request, "my_card/set_delete.html", {"someset": someset})

def wordpage(request, smth):
    someword = Word.objects.get(id=smth)
    return render(request, "my_card/word.html", {"someword":someword})

def add(request, id):

    # index sahifasiga POST metod yordamida o'tilgan bo'lsa
    if request.method == 'POST':
        add_word_form = WordForm(request.POST)
        # Check if the form is valid
        if add_word_form.is_valid():
            # Manually set the 'set' value before saving
            add_word_form.instance.set_id_id = id
            band = add_word_form.save()
            # if the form is not valid, we let execution continue to the return
    else:
        # Display an empty form for GET requests
        pass

    add_word_form = WordForm()

    return render(request, "my_card/word_add.html", {'add_word_form':add_word_form, 'id':id})

def delete(request, id):
    someword = Word.objects.get(id=id) # we need this for both GET and POST

    if request.method == 'POST':
        #unit o'zgaruvchi set_listda qolishimiz uchun kerak
        unit = someword.set_id.id
        someword.delete()

        # redirect to the wordpage
        return redirect('set_list', unit)
    # no need for an `else` here. If it's a GET request, just continue

    return render(request, "my_card/word_delete.html", {"someword": someword})

def update(request, id):
    someword = Word.objects.get(id=id)
    form=WordForm(instance=someword)
    if request.method == "POST":
        form = WordForm(request.POST,  instance=someword) # prepopulate the form with an existing band
        if form.is_valid():
            #update the existing word
            form.save()
            return redirect('wordpage', someword.id)
        else:
            form = WordForm(instance=someword)

    return render(request, "my_card/word_update.html", {"form": form})

#for testing
def testing(request):
  template = loader.get_template('my_card/template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))

