# Generated by Django 4.2 on 2023-09-09 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='product_id',
            new_name='msg_id',
        ),
    ]
