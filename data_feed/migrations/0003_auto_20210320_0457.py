# Generated by Django 2.2.12 on 2021-03-20 04:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_feed', '0002_auto_20210319_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprof',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
