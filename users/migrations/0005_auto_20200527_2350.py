# Generated by Django 3.0.6 on 2020-05-28 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200527_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sailstudent',
            old_name='is_admitted',
            new_name='admitted_student',
        ),
    ]
