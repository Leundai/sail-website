# Generated by Django 3.0.6 on 2020-05-29 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_sailuser_role'),
        ('courses', '0006_auto_20200528_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.Teacher'),
            preserve_default=False,
        ),
    ]
