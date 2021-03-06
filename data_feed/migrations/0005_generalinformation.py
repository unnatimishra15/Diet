# Generated by Django 3.0.8 on 2021-03-27 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_feed', '0004_smparentsprof'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_volunteer', models.CharField(blank=True, max_length=255)),
                ('name_of_student', models.CharField(blank=True, max_length=255)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('birthdate', models.DateField(max_length=20, null=True)),
                ('residential_address', models.CharField(max_length=2000, null=True)),
                ('pincode', models.CharField(blank=True, max_length=10)),
                ('name_of_school', models.CharField(blank=True, max_length=255)),
                ('address_of_school', models.CharField(blank=True, max_length=255)),
                ('pincode_of_school', models.CharField(blank=True, max_length=10)),
                ('personal_contact_number', models.CharField(blank=True, max_length=20)),
                ('religion', models.CharField(blank=True, choices=[('Hinduism', 'Hinduism'), ('Islam', 'Islam'), ('Christianity', 'Christianity'), ('Sikhism', 'Sikhism'), ('Jainism', 'Jainism'), ('Buddhism', 'Buddhism'), ('Other', 'Other')], max_length=20)),
            ],
        ),
    ]
