# Generated by Django 4.0.5 on 2022-07-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersession',
            name='expired_at',
            field=models.DateTimeField(null=True),
        ),
    ]
