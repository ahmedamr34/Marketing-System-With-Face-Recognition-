# Generated by Django 4.2 on 2023-06-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PorName', models.CharField(max_length=255)),
                ('PorDisc', models.TextField()),
                ('PorImg', models.ImageField(upload_to='Service_images/')),
            ],
        ),
    ]
