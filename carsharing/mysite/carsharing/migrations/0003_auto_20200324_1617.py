# Generated by Django 3.0.4 on 2020-03-24 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsharing', '0002_auto_20200324_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carsharing.Usuario'),
        ),
    ]
