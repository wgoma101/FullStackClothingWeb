# Generated by Django 4.2.6 on 2023-10-29 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_shirt_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='is_bestseller',
            field=models.BooleanField(default=False),
        ),
    ]
