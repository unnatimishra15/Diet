# Generated by Django 2.2.12 on 2021-03-10 10:13

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20210310_0323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anemicadolescentgirl',
            name='id',
        ),
        migrations.RemoveField(
            model_name='anemiclactatingmother',
            name='id',
        ),
        migrations.RemoveField(
            model_name='anemicpregnantwoman',
            name='id',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='nutrigardenexpert',
            name='id',
        ),
        migrations.RemoveField(
            model_name='nutritionexpert',
            name='id',
        ),
        migrations.RemoveField(
            model_name='principalinvestigators',
            name='id',
        ),
        migrations.RemoveField(
            model_name='projectmanager',
            name='id',
        ),
        migrations.RemoveField(
            model_name='schoolcoordinator',
            name='id',
        ),
        migrations.RemoveField(
            model_name='smchild',
            name='id',
        ),
        migrations.RemoveField(
            model_name='smchildparentsregister',
            name='id',
        ),
        migrations.RemoveField(
            model_name='webgisexpert',
            name='id',
        ),
        migrations.AlterField(
            model_name='anemicadolescentgirl',
            name='annualincome',
            field=models.CharField(choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='anemicadolescentgirl',
            name='education',
            field=models.CharField(choices=[('Professionaldegree', 'Professionaldegree'), ('Graduate', 'Graduate (Bachelors)'), ('Middleschool', 'Middle school (5th to 10th std)'), ('Primaryschool', 'Primary school (1st to 4th std)'), ('Illiterate', 'Illiterate (No education)')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='anemicadolescentgirl',
            name='heightunit',
            field=models.CharField(choices=[('kgs', 'kgs'), ('lbs', 'lbs')], max_length=255),
        ),
        migrations.AlterField(
            model_name='anemicadolescentgirl',
            name='occupation',
            field=models.CharField(choices=[('Legislators,Senior Officials & Managers', 'Legislators,Senior Officials & Managers'), ('Professionals', 'Professionals'), ('Technicians and Associate Professionals', 'Technicians and Associate Professionals'), ('Clerks', 'Clerks'), ('Skilled workers and Shop & Market sales workers ', 'Skilled workers and Shop & Market sales workers '), ('Skilled Agricultural', 'Skilled Agricultural and Fishery workers'), ('Craft and Related Trade Workers', 'Craft and Related Trade Workers'), ('Plant and Machine Operators and Assemblers', 'Plant and Machine Operators and Assemblers'), ('Elementary Occupation', 'Elementary Occupation'), ('Security guard', 'Security guard'), ('Housekeeper or Housemaid', 'Housekeeper or Housemaid'), ('Nurse', 'Nurse'), ('Anganwadi Worker', 'Anganwadi Worker'), ('Retired', 'Retired'), ('Others', 'Others')], max_length=2550),
        ),
        migrations.AlterField(
            model_name='anemicadolescentgirl',
            name='uid',
            field=models.CharField(default=False, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='anemicadolescentgirl',
            name='weightunit',
            field=models.CharField(choices=[('kgs', 'kgs'), ('lbs', 'lbs')], max_length=255),
        ),
        migrations.AlterField(
            model_name='anemiclactatingmother',
            name='annualincome',
            field=models.CharField(choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='anemiclactatingmother',
            name='education',
            field=models.CharField(choices=[('Professionaldegree', 'Professionaldegree'), ('Graduate', 'Graduate (Bachelors)'), ('Middleschool', 'Middle school (5th to 10th std)'), ('Primaryschool', 'Primary school (1st to 4th std)'), ('Illiterate', 'Illiterate (No education)')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='anemiclactatingmother',
            name='heightunit',
            field=models.CharField(choices=[('kgs', 'kgs'), ('lbs', 'lbs')], max_length=255),
        ),
        migrations.AlterField(
            model_name='anemiclactatingmother',
            name='occupation',
            field=models.CharField(choices=[('Legislators,Senior Officials & Managers', 'Legislators,Senior Officials & Managers'), ('Professionals', 'Professionals'), ('Technicians and Associate Professionals', 'Technicians and Associate Professionals'), ('Clerks', 'Clerks'), ('Skilled workers and Shop & Market sales workers ', 'Skilled workers and Shop & Market sales workers '), ('Skilled Agricultural', 'Skilled Agricultural and Fishery workers'), ('Craft and Related Trade Workers', 'Craft and Related Trade Workers'), ('Plant and Machine Operators and Assemblers', 'Plant and Machine Operators and Assemblers'), ('Elementary Occupation', 'Elementary Occupation'), ('Security guard', 'Security guard'), ('Housekeeper or Housemaid', 'Housekeeper or Housemaid'), ('Nurse', 'Nurse'), ('Anganwadi Worker', 'Anganwadi Worker'), ('Retired', 'Retired'), ('Others', 'Others')], max_length=2550),
        ),
        migrations.AlterField(
            model_name='anemiclactatingmother',
            name='uid',
            field=models.CharField(default=False, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='anemiclactatingmother',
            name='weightunit',
            field=models.CharField(choices=[('kgs', 'kgs'), ('lbs', 'lbs')], max_length=255),
        ),
        migrations.AlterField(
            model_name='anemicpregnantwoman',
            name='annualincome',
            field=models.CharField(choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='anemicpregnantwoman',
            name='education',
            field=models.CharField(choices=[('Professionaldegree', 'Professionaldegree'), ('Graduate', 'Graduate (Bachelors)'), ('Middleschool', 'Middle school (5th to 10th std)'), ('Primaryschool', 'Primary school (1st to 4th std)'), ('Illiterate', 'Illiterate (No education)')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='anemicpregnantwoman',
            name='feedback',
            field=models.CharField(max_length=2550),
        ),
        migrations.AlterField(
            model_name='anemicpregnantwoman',
            name='heightunit',
            field=models.CharField(choices=[('kgs', 'kgs'), ('lbs', 'lbs')], max_length=255),
        ),
        migrations.AlterField(
            model_name='anemicpregnantwoman',
            name='occupation',
            field=models.CharField(choices=[('Legislators,Senior Officials & Managers', 'Legislators,Senior Officials & Managers'), ('Professionals', 'Professionals'), ('Technicians and Associate Professionals', 'Technicians and Associate Professionals'), ('Clerks', 'Clerks'), ('Skilled workers and Shop & Market sales workers ', 'Skilled workers and Shop & Market sales workers '), ('Skilled Agricultural', 'Skilled Agricultural and Fishery workers'), ('Craft and Related Trade Workers', 'Craft and Related Trade Workers'), ('Plant and Machine Operators and Assemblers', 'Plant and Machine Operators and Assemblers'), ('Elementary Occupation', 'Elementary Occupation'), ('Security guard', 'Security guard'), ('Housekeeper or Housemaid', 'Housekeeper or Housemaid'), ('Nurse', 'Nurse'), ('Anganwadi Worker', 'Anganwadi Worker'), ('Retired', 'Retired'), ('Others', 'Others')], max_length=2550),
        ),
        migrations.AlterField(
            model_name='anemicpregnantwoman',
            name='uid',
            field=models.CharField(default=False, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='anemicpregnantwoman',
            name='weightunit',
            field=models.CharField(choices=[('kgs', 'kgs'), ('lbs', 'lbs')], max_length=255),
        ),
        migrations.AlterField(
            model_name='anganwadiworkersregister',
            name='anganwadiaddress',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='anganwadiworkersregister',
            name='anganwadiname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='anganwadiworkersregister',
            name='annualincome',
            field=models.CharField(blank=True, choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=25500),
        ),
        migrations.AlterField(
            model_name='anganwadiworkersregister',
            name='contact',
            field=models.CharField(blank=True, max_length=25500),
        ),
        migrations.AlterField(
            model_name='anganwadiworkersregister',
            name='uid',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='bulk_reg',
            name='mobile',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bulk_reg',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='concentform',
            name='concent',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='age',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='contact',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='education',
            field=models.CharField(choices=[('Professionaldegree', 'Professionaldegree'), ('Graduate', 'Graduate (Bachelors)'), ('Middleschool', 'Middle school (5th to 10th std)'), ('Primaryschool', 'Primary school (1st to 4th std)'), ('Illiterate', 'Illiterate (No education)')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='uid',
            field=models.CharField(default=False, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mukhyasevika',
            name='annualincome',
            field=models.CharField(blank=True, choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=25500),
        ),
        migrations.AlterField(
            model_name='mukhyasevika',
            name='birthdate',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='mukhyasevika',
            name='contact',
            field=models.CharField(blank=True, max_length=25500),
        ),
        migrations.AlterField(
            model_name='mukhyasevika',
            name='uid',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='nutrigardenexpert',
            name='age',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='nutrigardenexpert',
            name='contact',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='nutrigardenexpert',
            name='uid',
            field=models.CharField(default=False, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nutritionexpert',
            name='age',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='nutritionexpert',
            name='contact',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='nutritionexpert',
            name='uid',
            field=models.CharField(default=False, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='principalinvestigators',
            name='age',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='principalinvestigators',
            name='contact',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='principalinvestigators',
            name='uid',
            field=models.CharField(default=False, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projectmanager',
            name='age',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='projectmanager',
            name='contact',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='projectmanager',
            name='uid',
            field=models.CharField(default=False, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='school',
            name='contact',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='schoolcoordinator',
            name='annualincome',
            field=models.CharField(blank=True, choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=25500),
        ),
        migrations.AlterField(
            model_name='schoolcoordinator',
            name='contact',
            field=models.CharField(blank=True, max_length=25500),
        ),
        migrations.AlterField(
            model_name='schoolcoordinator',
            name='schoolcontact',
            field=models.CharField(blank=True, max_length=25500),
        ),
        migrations.AlterField(
            model_name='schoolcoordinator',
            name='uid',
            field=models.CharField(default=False, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='schoolstudentparent',
            name='annualincome',
            field=models.CharField(blank=True, choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=25500),
        ),
        migrations.AlterField(
            model_name='schoolstudentparent',
            name='contact',
            field=models.CharField(blank=True, max_length=25500),
        ),
        migrations.AlterField(
            model_name='schoolstudentparent',
            name='foodhabits',
            field=models.CharField(blank=True, choices=[('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian')], max_length=25500),
        ),
        migrations.AlterField(
            model_name='schoolstudentparent',
            name='personaladdress',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='schoolstudentparent',
            name='schoolcontact',
            field=models.CharField(blank=True, max_length=25500),
        ),
        migrations.AlterField(
            model_name='schoolstudentparent',
            name='schoolcoordinatorincharge',
            field=models.CharField(blank=True, max_length=25500),
        ),
        migrations.AlterField(
            model_name='schoolstudentparent',
            name='schoolname',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='schoolstudentparent',
            name='uid',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='smchild',
            name='age',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='smchild',
            name='heightunit',
            field=models.CharField(choices=[('kgs', 'kgs'), ('lbs', 'lbs')], max_length=255),
        ),
        migrations.AlterField(
            model_name='smchild',
            name='uid',
            field=models.CharField(default=False, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='smchild',
            name='weightunit',
            field=models.CharField(choices=[('kgs', 'kgs'), ('lbs', 'lbs')], max_length=255),
        ),
        migrations.AlterField(
            model_name='smchildparentsregister',
            name='annualincome',
            field=models.CharField(choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='smchildparentsregister',
            name='cuid',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='smchildparentsregister',
            name='education',
            field=models.CharField(choices=[('Professionaldegree', 'Professionaldegree'), ('Graduate', 'Graduate (Bachelors)'), ('Middleschool', 'Middle school (5th to 10th std)'), ('Primaryschool', 'Primary school (1st to 4th std)'), ('Illiterate', 'Illiterate (No education)')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='smchildparentsregister',
            name='fatherbirthdate',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='smchildparentsregister',
            name='fathername',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='smchildparentsregister',
            name='motherbirthdate',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='smchildparentsregister',
            name='mothername',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='smchildparentsregister',
            name='occupation',
            field=models.CharField(choices=[('Legislators,Senior Officials & Managers', 'Legislators,Senior Officials & Managers'), ('Professionals', 'Professionals'), ('Technicians and Associate Professionals', 'Technicians and Associate Professionals'), ('Clerks', 'Clerks'), ('Skilled workers and Shop & Market sales workers ', 'Skilled workers and Shop & Market sales workers '), ('Skilled Agricultural', 'Skilled Agricultural and Fishery workers'), ('Craft and Related Trade Workers', 'Craft and Related Trade Workers'), ('Plant and Machine Operators and Assemblers', 'Plant and Machine Operators and Assemblers'), ('Elementary Occupation', 'Elementary Occupation'), ('Security guard', 'Security guard'), ('Housekeeper or Housemaid', 'Housekeeper or Housemaid'), ('Nurse', 'Nurse'), ('Anganwadi Worker', 'Anganwadi Worker'), ('Retired', 'Retired'), ('Others', 'Others')], max_length=2550),
        ),
        migrations.AlterField(
            model_name='smchildparentsregister',
            name='uid',
            field=models.CharField(default=False, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=25500)),
        ),
        migrations.AlterField(
            model_name='student',
            name='heightunit',
            field=models.CharField(choices=[('kgs', 'kgs'), ('lbs', 'lbs')], default=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='uid',
            field=models.CharField(max_length=25500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='weightunit',
            field=models.CharField(choices=[('kgs', 'kgs'), ('lbs', 'lbs')], default=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='webgisexpert',
            name='age',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='webgisexpert',
            name='contact',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='webgisexpert',
            name='uid',
            field=models.CharField(default=False, max_length=255, primary_key=True, serialize=False),
        ),
    ]
