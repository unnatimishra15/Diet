# Generated by Django 2.2.12 on 2021-03-03 11:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='bulk_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('dob', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConcentForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concent', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalExpert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SupportMentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('mentortype', models.CharField(choices=[('Head Mentor', 'Head Mentor'), ('Support Mentor', 'Support Mentor')], default=False, max_length=20)),
                ('category', models.CharField(choices=[('Parent', 'Parent'), ('Teacher', 'Teacher'), ('Student', 'Student')], default=False, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nutrileader', models.CharField(choices=[('Nutri-Leader', 'Nutri-Leader'), ('School-Student', 'School-Student')], default=False, max_length=20)),
                ('contact', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=1000))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SMChildRegistration',
            fields=[
                ('uid', models.CharField(default=1, max_length=100, primary_key=True, serialize=False)),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SMChildParentsDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuid', models.CharField(max_length=10)),
                ('mothername', models.CharField(max_length=50)),
                ('fathername', models.CharField(max_length=50)),
                ('mage', models.IntegerField()),
                ('fage', models.IntegerField()),
                ('fatheroccupation', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=50, null=True)),
                ('monthlyincome', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolCoordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=1000)),
                ('schoolname', models.CharField(max_length=2000)),
                ('personaladdress', models.CharField(max_length=2000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('name', models.CharField(max_length=200, null=True)),
                ('institute', models.CharField(choices=[('Organization', 'Organization'), ('College', 'College'), ('School', 'School')], default=False, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCoordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PregnantWomanRegistration',
            fields=[
                ('uid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NutriGardenExpert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MukhyaSevika',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('dob', models.DateField(blank=True, default=datetime.datetime.now)),
                ('age', models.CharField(default=0, max_length=6, null=True)),
                ('age_in_months', models.CharField(default=0, max_length=6, null=True)),
                ('age_in_days', models.CharField(default=0, max_length=6, null=True)),
                ('personaladdress', models.CharField(max_length=200, null=True)),
                ('anganwadinumber', models.IntegerField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HeadMentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('mentortype', models.CharField(choices=[('Head Mentor', 'Head Mentor'), ('Support Mentor', 'Support Mentor')], default=False, max_length=20)),
                ('institute', models.CharField(choices=[('Organization', 'Organization'), ('College', 'College'), ('School', 'School')], default=False, max_length=20)),
                ('qualification', models.CharField(choices=[('BSc', 'BSc'), ('BSW', 'BSW')], default=False, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnganwadiWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, default=datetime.datetime.now)),
                ('age', models.CharField(default=0, max_length=6, null=True)),
                ('age_in_months', models.CharField(default=0, max_length=6, null=True)),
                ('age_in_days', models.CharField(default=0, max_length=6, null=True)),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('anganwadiname', models.CharField(max_length=200, null=True)),
                ('personaladdress', models.CharField(max_length=200, null=True)),
                ('anganwadiaddress', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnemicWomanRegistration',
            fields=[
                ('uid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdolescentGirlRegistration',
            fields=[
                ('uid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
