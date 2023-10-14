# Generated by Django 4.2.4 on 2023-10-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindifyServer', '0004_rename_first_name_user_name_remove_user_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='lostitem',
            name='tags',
            field=models.ManyToManyField(to='FindifyServer.tag'),
        ),
    ]
