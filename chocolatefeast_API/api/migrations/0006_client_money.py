# Generated by Django 4.0.5 on 2022-06-18 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='money',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
