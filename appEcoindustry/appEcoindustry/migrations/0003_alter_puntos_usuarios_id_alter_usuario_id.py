# Generated by Django 4.0.6 on 2022-09-12 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEcoindustry', '0002_remove_bonificacion_cantidad_bonificacion_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puntos_usuarios',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
