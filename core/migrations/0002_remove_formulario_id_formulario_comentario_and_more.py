# Generated by Django 4.2.1 on 2023-06-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='id',
        ),
        migrations.AddField(
            model_name='formulario',
            name='comentario',
            field=models.CharField(default='Sin comentario', max_length=50, verbose_name='Comentario'),
        ),
        migrations.AddField(
            model_name='formulario',
            name='idFormulario',
            field=models.CharField(default=0, max_length=10, primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='apellido',
            field=models.CharField(max_length=30, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='cantidad_personas',
            field=models.CharField(max_length=2, verbose_name='Cantidad personas'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='correo',
            field=models.CharField(max_length=30, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='fecha_reserva',
            field=models.CharField(max_length=10, verbose_name='Fecha reserva'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='telefono',
            field=models.CharField(max_length=9, verbose_name='Telefono'),
        ),
    ]