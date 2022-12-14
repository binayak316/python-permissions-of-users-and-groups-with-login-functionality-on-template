# Generated by Django 4.1.3 on 2022-11-18 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_contact', models.CharField(max_length=15)),
                ('emp_salary', models.FloatField()),
            ],
        ),
    ]
