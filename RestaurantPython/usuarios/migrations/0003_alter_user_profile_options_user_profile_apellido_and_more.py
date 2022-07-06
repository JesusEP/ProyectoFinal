# Generated by Django 4.0.4 on 2022-07-06 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_rename_user_user_profile_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_profile',
            options={'verbose_name': 'perfil', 'verbose_name_plural': 'perfiles'},
        ),
        migrations.AddField(
            model_name='user_profile',
            name='apellido',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='nombre',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='sitio_web',
            field=models.URLField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
