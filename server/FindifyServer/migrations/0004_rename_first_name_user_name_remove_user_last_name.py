# Generated by Django 4.2.4 on 2023-10-11 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FindifyServer', '0003_alter_founditem_finder_alter_lostitem_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
