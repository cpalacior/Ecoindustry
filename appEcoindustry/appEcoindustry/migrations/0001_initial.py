# Generated by Django 4.1 on 2022-08-19 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bonificacion",
            fields=[
                ("idbonificacion", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=30)),
                ("valor", models.IntegerField()),
                ("cantidad", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="TipoUsuario",
            fields=[
                (
                    "idtipousuario",
                    models.SmallIntegerField(primary_key=True, serialize=False),
                ),
                ("desctipousuario", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("nombreEmpresa", models.CharField(max_length=45)),
                ("NIT", models.BigIntegerField()),
                ("correo", models.CharField(max_length=45)),
                ("clave", models.CharField(max_length=30)),
                ("direccion", models.CharField(max_length=50)),
                (
                    "idtipousuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appEcoindustry.tipousuario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usuario_Bonificacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "idbonificacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appEcoindustry.bonificacion",
                    ),
                ),
                (
                    "identificacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appEcoindustry.usuario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Puntos_Usuarios",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cantidad", models.IntegerField()),
                (
                    "identificacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appEcoindustry.usuario",
                    ),
                ),
            ],
        ),
    ]
