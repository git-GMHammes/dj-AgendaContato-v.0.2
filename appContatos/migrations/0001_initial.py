# Generated by Django 4.0 on 2021-12-11 20:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DbTabCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DbTabContatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strNome', models.CharField(max_length=255)),
                ('strSobreNome', models.CharField(blank=True, max_length=255)),
                ('strEmail', models.CharField(blank=True, max_length=255)),
                ('strDataCriacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('TexDescricao', models.TextField(blank=True)),
                ('keyTabCategoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appContatos.dbtabcategoria')),
            ],
        ),
    ]
