# Generated by Django 3.2.8 on 2022-01-01 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('meal', '0004_auto_20211223_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.customer'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
