# Generated by Django 4.2.6 on 2023-10-24 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_card', '0002_alter_flashword_defenition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashword',
            name='defenition',
            field=models.TextField(null=True),
        ),
    ]
