# Generated by Django 3.2.7 on 2021-10-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_noticias_categoria_noticia'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='previa_noticia',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
