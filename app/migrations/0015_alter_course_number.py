# Generated by Django 4.1.2 on 2022-12-22 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_section_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='number',
            field=models.CharField(max_length=3),
        ),
    ]