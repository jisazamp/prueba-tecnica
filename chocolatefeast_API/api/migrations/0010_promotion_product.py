# Generated by Django 4.0.5 on 2022-06-18 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_rename_promotions_promotion_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="promotion",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.product"
            ),
        ),
    ]
