# Generated by Django 3.2.9 on 2021-11-08 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='imgURL',
            field=models.URLField(blank=True, null=True),
        ),
    ]