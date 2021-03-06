# Generated by Django 4.0.5 on 2022-06-18 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_money_client_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('numberOfWraps', models.PositiveIntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.store')),
            ],
        ),
    ]
