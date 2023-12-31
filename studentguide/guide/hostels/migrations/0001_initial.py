# Generated by Django 4.2 on 2023-06-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_number', models.CharField(max_length=2, verbose_name='Hostel Number')),
                ('hostel_photo', models.ImageField(upload_to='hostels/', verbose_name='Hostel Photo')),
                ('price_for_scholarship', models.IntegerField(verbose_name='Price For Scholarship')),
                ('price_for_paid_basis', models.IntegerField(verbose_name='Price for paid basis')),
                ('floors', models.IntegerField(verbose_name='Floors')),
                ('gym', models.BooleanField(default=False, verbose_name='Gym')),
                ('type', models.CharField(max_length=128, verbose_name='Type')),
                ('coworking', models.BooleanField(default=False, verbose_name='Coworking')),
                ('kitchens', models.CharField(max_length=32, verbose_name='Kitchens')),
                ('washers', models.CharField(max_length=32, verbose_name='Washers')),
                ('adress', models.CharField(max_length=256, verbose_name='Address')),
                ('dryers', models.IntegerField(verbose_name='Dryers')),
                ('to_pryaniki', models.CharField(max_length=64, verbose_name='To Pryaniki')),
                ('to_pk', models.CharField(max_length=64, verbose_name='To PK')),
                ('to_bs', models.CharField(max_length=64, verbose_name='To BS')),
                ('to_mikhalka', models.CharField(max_length=64, verbose_name='To Mikhalka')),
                ('to_avtovaz', models.CharField(max_length=64, verbose_name='To Avtovaz')),
            ],
        ),
    ]
