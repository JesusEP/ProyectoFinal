# Generated by Django 4.0.5 on 2022-06-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('precio', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
