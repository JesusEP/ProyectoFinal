# Generated by Django 4.0.4 on 2022-06-08 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradas',
            name='descripcion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
