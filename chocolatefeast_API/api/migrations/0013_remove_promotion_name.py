# Generated by Django 4.0.5 on 2022-06-18 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_order_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='name',
        ),
    ]
