# Generated by Django 4.0.3 on 2022-03-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='profiles/')),
                ('bio', models.TextField()),
                ('contact_info', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('website_picture', models.ImageField(upload_to='uploads/')),
                ('description', models.TextField()),
                ('website_link', models.CharField(max_length=255)),
            ],
        ),
    ]
