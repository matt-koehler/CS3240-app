# Generated by Django 3.1.5 on 2021-03-29 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0006_auto_20210324_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='isCompleted',
            new_name='isReported',
        ),
    ]