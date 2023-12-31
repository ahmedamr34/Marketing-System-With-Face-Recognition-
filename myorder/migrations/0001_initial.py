# Generated by Django 4.2 on 2023-06-14 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('websites', '0001_initial'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cat_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('brand_name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('product_description', models.CharField(max_length=500)),
                ('place', models.CharField(default='null', max_length=500)),
                ('image', models.ImageField(upload_to='order_images')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
                ('AddHolder_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_AddHolder', to='websites.addholder')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_Category', to='myorder.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.regularuserproxy', to_field='username')),
            ],
        ),
    ]
