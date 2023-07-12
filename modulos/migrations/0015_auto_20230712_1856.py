# Generated by Django 3.2.19 on 2023-07-12 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0014_auto_20230712_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_curso', models.CharField(max_length=100)),
                ('cant_alumnos', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='institucion',
            name='cant_alumnos',
        ),
        migrations.RemoveField(
            model_name='institucion',
            name='nombre_curso',
        ),
        migrations.AddField(
            model_name='institucion',
            name='curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='modulos.curso'),
            preserve_default=False,
        ),
    ]