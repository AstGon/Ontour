# Generated by Django 3.2.19 on 2023-06-13 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id_archivo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('ruta', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ejecutivo',
            fields=[
                ('id_ejecutivo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_eje', models.CharField(max_length=100)),
                ('apellido_eje', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicios', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoArchivo',
            fields=[
                ('id_tipo_archivo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id_contrato', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('fecha_contrato', models.DateField()),
                ('nombre_curso', models.CharField(max_length=100)),
                ('cant_alumnos', models.IntegerField()),
                ('colegio', models.CharField(max_length=100)),
                ('rut_rep_legal', models.CharField(max_length=100)),
                ('nombre_rep_legal', models.CharField(max_length=100)),
                ('archivos', models.ManyToManyField(to='modulos.Archivo')),
                ('ejecutivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.ejecutivo')),
                ('servicios', models.ManyToManyField(to='modulos.Servicio')),
            ],
        ),
        migrations.AddField(
            model_name='archivo',
            name='tipo_archivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.tipoarchivo'),
        ),
    ]
