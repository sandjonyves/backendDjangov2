# Generated by Django 4.2.2 on 2023-07-07 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataEncadreur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('prenom', models.CharField(max_length=150)),
                ('numTel', models.CharField(max_length=15)),
                ('addEmail', models.EmailField(max_length=250, unique=True)),
                ('untEnseignaement', models.CharField(max_length=250)),
            ],
        ),
    ]