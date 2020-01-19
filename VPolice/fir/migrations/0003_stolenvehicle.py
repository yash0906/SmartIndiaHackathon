# Generated by Django 3.0 on 2020-01-19 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0002_auto_20200119_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='StolenVehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_type', models.CharField(choices=[('Car', 'Car'), ('Truck', 'Truck'), ('Bike', 'Bike'), ('Scooter', 'Scooter')], default='Car', max_length=200)),
                ('reg_num', models.CharField(max_length=200)),
                ('eng_num', models.CharField(max_length=200)),
                ('chassis_num', models.CharField(max_length=200)),
            ],
        ),
    ]