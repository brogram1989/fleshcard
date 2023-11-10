from django.db import models

# Create your models here.



class Set(models.Model):
    name = models.CharField(max_length = 64)
    description = models.CharField(max_length = 255, blank =True)


    def __str__(self):
        return f"{self.name}"



class Word(models.Model):
    word = models.CharField(max_length=100)
    translate = models.CharField(max_length=255)
    defenition = models.TextField(blank=True)
    set_id = models.ForeignKey(Set, on_delete=models.CASCADE, related_name='word_set')

    def __str__(self):
        return f"{self.word} - {self.translate}"

