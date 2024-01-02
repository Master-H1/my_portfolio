# Generated by Django 4.2.6 on 2023-12-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_alter_projects_description1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='technology_used',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='option',
            field=models.CharField(choices=[('Front-End Development', 'Front-End Development'), ('OtherSkills', 'OtherSkills'), ('Back-End Development', 'Back-End Development')], max_length=100),
        ),
    ]
