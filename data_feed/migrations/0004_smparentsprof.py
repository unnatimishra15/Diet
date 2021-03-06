# Generated by Django 3.0.8 on 2021-03-21 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data_feed', '0003_auto_20210321_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='smparentsprof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100, null=True)),
                ('birthdate', models.CharField(max_length=2000, null=True)),
                ('age', models.CharField(blank=True, max_length=200)),
                ('education', models.CharField(blank=True, choices=[('Professionaldegree', 'Professionaldegree'), ('Graduate', 'Graduate (Bachelors)'), ('Middleschool', 'Middle school (5th to 10th std)'), ('Primaryschool', 'Primary school (1st to 4th std)'), ('Illiterate', 'Illiterate (No education)')], max_length=2000)),
                ('occupation', models.CharField(blank=True, choices=[('Legislators,Senior Officials & Managers', 'Legislators,Senior Officials & Managers'), ('Professionals', 'Professionals'), ('Technicians and Associate Professionals', 'Technicians and Associate Professionals'), ('Clerks', 'Clerks'), ('Skilled workers and Shop & Market sales workers ', 'Skilled workers and Shop & Market sales workers '), ('Skilled Agricultural', 'Skilled Agricultural and Fishery workers'), ('Craft and Related Trade Workers', 'Craft and Related Trade Workers'), ('Plant and Machine Operators and Assemblers', 'Plant and Machine Operators and Assemblers'), ('Elementary Occupation', 'Elementary Occupation'), ('Security guard', 'Security guard'), ('Housekeeper or Housemaid', 'Housekeeper or Housemaid'), ('Nurse', 'Nurse'), ('Anganwadi Worker', 'Anganwadi Worker'), ('Retired', 'Retired'), ('Others', 'Others')], max_length=2000)),
                ('annualincome', models.CharField(blank=True, choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=25500)),
                ('ICDSname', models.CharField(max_length=200)),
                ('ICDScenteraddress', models.CharField(max_length=200)),
                ('ICDScentercontact', models.CharField(max_length=200)),
                ('foodhabits', models.CharField(choices=[('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian')], max_length=20, null=True)),
                ('profile_photo', models.ImageField(blank=True, upload_to='SMParents/%Y/%m/%d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
