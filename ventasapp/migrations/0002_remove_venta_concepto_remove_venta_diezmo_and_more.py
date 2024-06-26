# Generated by Django 5.0.6 on 2024-06-14 21:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='concepto',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='diezmo',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='ganancia_14',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='ganancia_28',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='inversion',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='publicidad',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='total',
        ),
        migrations.AddField(
            model_name='venta',
            name='producto',
            field=models.CharField(default='Producto desconocido', max_length=100),
        ),
        migrations.AddField(
            model_name='venta',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='venta',
            name='cantidad',
            field=models.IntegerField(),
        ),
    ]
