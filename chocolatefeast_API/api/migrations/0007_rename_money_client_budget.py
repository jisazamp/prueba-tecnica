# Generated by Django 4.0.5 on 2022-06-18 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_client_money'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='money',
            new_name='budget',
        ),
    ]
