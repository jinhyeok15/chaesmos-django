# Generated by Django 4.0.5 on 2022-08-15 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usersession_expired_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='nickname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
