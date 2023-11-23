from django import forms
from .models import Word, Set


class SetForm(forms.ModelForm):
    class Meta:
        model = Set   #qaysi model uchun forma yasayotganimizni ko'rsatamiz
        fields = '__all__'

class WordForm(forms.ModelForm):
    class Meta:

        model = Word #qaysi model uchun forma yasayotganimizni ko'rsatamiz
        #fields = '__all__' #agar barcha polyalarni qo'yishni istamasak buni o'chirsak, excludeni ishlatishimiz mn
        exclude = ['set_id']  # set_id polyasidan boshqa barcha polyalar uchun forma yaratadi

        # ModelForm qilmasdan forms.Form orqalik xam qilsa bo'ladi bu soddaroq, lekin xar bir model uchun
        # alohida charfield, textfiled , datefield yoki imagefieldlarni yozib chiqamiz,
        # model o'zgarganda esa formani xam o'zgartiramiz
        # forms.ModelForm ning qulayligi modelimiz o'zgarganda formani o'zgartirish shart emas
