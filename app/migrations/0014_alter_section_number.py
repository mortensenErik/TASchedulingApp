# Generated by Django 4.1.2 on 2022-12-21 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_course_courseid_alter_section_sectionid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='number',
            field=models.CharField(max_length=3),
        ),
    ]
