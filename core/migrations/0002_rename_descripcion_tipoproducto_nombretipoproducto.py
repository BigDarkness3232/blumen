# Generated by Django 4.2.1 on 2023-05-07 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipoproducto',
            old_name='descripcion',
            new_name='nombreTipoProducto',
        ),
    ]
