from django import forms
from .models import Word

class AddNew(forms.Form):
    word = forms.CharField(label='New word' , max_length=100)
    translate = forms.CharField(label='Translation' ,max_length=255)
    defenition = forms.CharField(label='Defenition', widget=forms.Textarea(attrs={'name':'defenition', 'rows':10, 'cols': 40}), required=False)



#AddNewning ikkinchi model bilan bog'langan ko'rinishini yasash
#bunda model o'zgargan taqdirda yangi forma xam o'zgaradi
class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__' #agar barcha polyalarni qo'yishni istamasak buni o'chirsak, excludeni ishlatishimiz mn
        #exclude = ('defenition')  # defenition polyasidan boshqa barcha polyalar uchun forma yaratadi