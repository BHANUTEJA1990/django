# Generated by Django 4.1.7 on 2023-03-20 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Iname',
            new_name='iname',
        ),
    ]