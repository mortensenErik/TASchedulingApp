# Generated by Django 4.1.2 on 2022-12-05 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='pw',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='username',
        ),
    ]
