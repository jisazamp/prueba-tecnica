# Generated by Django 4.0.5 on 2022-06-18 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_promotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='promotion',
            field=models.ManyToManyField(to='api.promotion'),
        ),
    ]
