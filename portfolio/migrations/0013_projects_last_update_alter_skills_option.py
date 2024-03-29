# Generated by Django 4.2.6 on 2023-12-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_projects_alter_skills_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='option',
            field=models.CharField(choices=[('Back-End Development', 'Back-End Development'), ('OtherSkills', 'OtherSkills'), ('Front-End Development', 'Front-End Development')], max_length=100),
        ),
    ]
