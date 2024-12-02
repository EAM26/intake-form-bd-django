# Generated by Django 5.1.3 on 2024-11-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('zip_code', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('requesting_party', models.CharField(max_length=80)),
                ('risk_class', models.CharField(max_length=80)),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
