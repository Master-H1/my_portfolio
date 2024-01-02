# Generated by Django 4.2.6 on 2023-12-28 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_rename_skills_opt_devskills_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(choices=[('Front-End Development', 'Front-End Development'), ('Other Skills', 'Other skills'), ('Back-End Development', 'Back-End Development')], max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.DeleteModel(
            name='DevSkills',
        ),
        migrations.DeleteModel(
            name='SkillsOption',
        ),
    ]
