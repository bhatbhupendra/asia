# Generated by Django 3.2.8 on 2022-01-22 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0006_optionone_optiononeoptions_optiontwo_optiontwooptions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='optionone',
            options={'verbose_name': 'Option One', 'verbose_name_plural': 'Option One'},
        ),
        migrations.AlterModelOptions(
            name='optiononeoptions',
            options={'verbose_name': 'Option One Items', 'verbose_name_plural': 'Option One Items'},
        ),
        migrations.AlterModelOptions(
            name='optiontwo',
            options={'verbose_name': 'Option Two', 'verbose_name_plural': 'Option Two'},
        ),
        migrations.AlterModelOptions(
            name='optiontwooptions',
            options={'verbose_name': 'Option Two Item', 'verbose_name_plural': 'Option Two Items'},
        ),
        migrations.AddField(
            model_name='meals',
            name='option',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
