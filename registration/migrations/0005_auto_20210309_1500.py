# Generated by Django 3.0.8 on 2021-03-09 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20210309_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anemicadolescentgirl',
            name='bmi',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='anemiclactatingmother',
            name='bmi',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='anemicpregnantwoman',
            name='bmi',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='smchild',
            name='bmi',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='bmi',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='whratio',
            field=models.IntegerField(default=0),
        ),
    ]
