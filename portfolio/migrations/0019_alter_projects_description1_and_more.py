# Generated by Django 4.2.6 on 2023-12-30 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_projects_description1_projects_description2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description1',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='in_short',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='option',
            field=models.CharField(choices=[('OtherSkills', 'OtherSkills'), ('Back-End Development', 'Back-End Development'), ('Front-End Development', 'Front-End Development')], max_length=100),
        ),
    ]
