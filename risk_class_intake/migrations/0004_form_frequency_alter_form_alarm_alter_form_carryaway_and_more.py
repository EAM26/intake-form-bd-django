# Generated by Django 5.1.3 on 2024-12-02 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_class_intake', '0003_rename_new_field_2_form_constructional_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='frequency',
            field=models.IntegerField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='alarm',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='carryaway',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='compartment',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='constructional',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='customization',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='electronic',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='email',
            field=models.EmailField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='maintenance',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='organizational',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='partial_security',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='reaction',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='shield',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='verification',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]