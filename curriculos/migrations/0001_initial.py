# Generated by Django 5.1.2 on 2024-10-30 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('linkedin', models.CharField(max_length=100)),
                ('personal_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact_info', to='curriculos.personalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=60)),
                ('course', models.CharField(max_length=60)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('personal_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_training', to='curriculos.personalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('personal_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experience', to='curriculos.personalinfo')),
            ],
        ),
    ]
