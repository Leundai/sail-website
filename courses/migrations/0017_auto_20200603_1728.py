# Generated by Django 3.0.6 on 2020-06-03 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_sailuser_role'),
        ('courses', '0016_auto_20200603_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.AddField(
            model_name='section',
            name='students',
            field=models.ManyToManyField(blank=True, to='users.Student'),
        ),
    ]
