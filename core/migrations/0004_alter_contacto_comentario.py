# Generated by Django 4.2.1 on 2023-06-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contacto_delete_formulario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='comentario',
            field=models.TextField(max_length=50),
        ),
    ]