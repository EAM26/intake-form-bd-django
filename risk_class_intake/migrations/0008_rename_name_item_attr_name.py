# Generated by Django 5.1.3 on 2024-12-03 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_class_intake', '0007_item_attractiveness'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='attr_name',
        ),
    ]
