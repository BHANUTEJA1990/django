# Generated by Django 4.1.7 on 2023-03-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='na', max_length=20),
            preserve_default=False,
        ),
    ]