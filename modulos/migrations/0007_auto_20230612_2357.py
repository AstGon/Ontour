# Generated by Django 3.2.19 on 2023-06-13 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0006_alter_servicio_id_servicios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivo',
            name='tipo_archivo',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='archivos',
        ),
        migrations.AddField(
            model_name='archivo',
            name='contrato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.contrato'),
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='servicios',
        ),
        migrations.AddField(
            model_name='contrato',
            name='servicios',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.servicio'),
        ),
    ]
