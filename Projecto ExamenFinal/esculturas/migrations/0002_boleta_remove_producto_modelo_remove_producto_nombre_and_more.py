# Generated by Django 4.2.2 on 2023-07-13 04:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esculturas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.BigIntegerField()),
                ('fechaCompra', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='modelo',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='nombre',
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio'),
        ),
        migrations.AddField(
            model_name='producto',
            name='producto',
            field=models.CharField(blank=True, max_length=50, verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio'),
        ),
        migrations.CreateModel(
            name='detalle_boleta',
            fields=[
                ('id_detalle_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.BigIntegerField()),
                ('id_boleta', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='esculturas.boleta')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esculturas.producto')),
            ],
        ),
    ]
