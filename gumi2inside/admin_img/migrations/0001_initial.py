# Generated by Django 4.2.5 on 2023-10-15 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel1', models.TextField()),
                ('carousel2', models.TextField()),
                ('carousel3', models.TextField()),
                ('logo', models.TextField()),
                ('bird', models.TextField()),
                ('status', models.TextField(default='Admin_img')),
            ],
        ),
    ]
