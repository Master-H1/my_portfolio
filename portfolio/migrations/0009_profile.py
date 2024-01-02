# Generated by Django 4.2.6 on 2023-12-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_skills_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='profile_pic')),
                ('role', models.CharField(max_length=100)),
            ],
        ),
    ]
