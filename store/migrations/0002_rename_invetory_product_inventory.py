# Generated by Django 4.1.2 on 2022-10-10 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='invetory',
            new_name='inventory',
        ),
    ]
