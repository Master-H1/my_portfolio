# Generated by Django 4.2.6 on 2023-12-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_skills_delete_devskills_delete_skillsoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='option',
            field=models.CharField(choices=[('Back-End Development', 'Back-End Development'), ('OtherSkills', 'OtherSkills'), ('Front-End Development', 'Front-End Development')], max_length=100),
        ),
    ]
