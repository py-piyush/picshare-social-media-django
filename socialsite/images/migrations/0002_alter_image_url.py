# Generated by Django 4.1.6 on 2023-02-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(blank=True, max_length=2000),
        ),
    ]