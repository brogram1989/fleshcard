# Generated by Django 4.2.6 on 2023-10-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashword',
            name='defenition',
            field=models.TextField(),
        ),
    ]
