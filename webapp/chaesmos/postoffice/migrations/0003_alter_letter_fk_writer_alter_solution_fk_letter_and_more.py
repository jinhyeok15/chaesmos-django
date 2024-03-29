# Generated by Django 4.0.5 on 2022-07-27 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usersession_expired_at'),
        ('postoffice', '0002_rename_seleted_date_letter_selected_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='fk_writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='letters', to='users.useraccount'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='fk_letter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='solutions', to='postoffice.letter'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='fk_sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='senders', to='users.useraccount'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='fk_letter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tags', to='postoffice.letter'),
        ),
    ]
