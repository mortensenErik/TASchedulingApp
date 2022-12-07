# Generated by Django 4.1.2 on 2022-12-07 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_section_number_alter_section_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='section',
            name='teacher',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='assignedTo',
            field=models.ManyToManyField(null=True, related_name='assignedToCourse', to='app.section'),
        ),
    ]