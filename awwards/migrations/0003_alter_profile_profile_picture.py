# Generated by Django 4.0.3 on 2022-03-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0002_profile_user_project_user_alter_profile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profiles/222.jpg', null=True, upload_to='profiles/'),
        ),
    ]
