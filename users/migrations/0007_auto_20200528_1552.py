# Generated by Django 3.0.6 on 2020-05-28 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200528_1552'),
        ('users', '0006_auto_20200528_0256'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SailStudent',
            new_name='Student',
        ),
        migrations.RenameModel(
            old_name='SailTeacher',
            new_name='Teacher',
        ),
    ]