# Generated by Django 4.2.6 on 2023-11-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_card', '0003_alter_flashword_defenition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('translate', models.CharField(max_length=255)),
                ('defenition', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FlashWord',
        ),
    ]
