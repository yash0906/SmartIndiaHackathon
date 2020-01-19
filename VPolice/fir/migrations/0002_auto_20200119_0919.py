# Generated by Django 3.0 on 2020-01-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='missingchildren',
            name='eye',
            field=models.CharField(choices=[('Black', 'Black'), ('Brown', 'Brown'), ('Blue', 'Blue')], default='Black', max_length=100),
        ),
        migrations.AddField(
            model_name='missingchildren',
            name='face',
            field=models.CharField(choices=[('Round', 'Round'), ('Injury Mark', 'Injury Mark'), ('Oval', 'Oval'), ('Small Pox', 'Small Pox'), ('Wrinkled', 'Wrinkled'), ('Forhead-Broad', 'Forhead-Broad'), ('Forhead-Narrow', 'Forhead-Narrow')], default='Round', max_length=100),
        ),
        migrations.AddField(
            model_name='missingchildren',
            name='hair',
            field=models.CharField(choices=[('Black', 'Black'), ('Brown', 'Brown'), ('White', 'White')], default='Black', max_length=100),
        ),
        migrations.AddField(
            model_name='missingchildren',
            name='missing_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='missingchildren',
            name='state',
            field=models.CharField(choices=[('Haryana', 'Haryana'), ('Rajasthan', 'Rajasthan'), ('Hyderabad', 'Hyderabad'), ('Delhi', 'Delhi')], default='Haryana', max_length=100),
        ),
        migrations.AlterField(
            model_name='missingchildren',
            name='sex',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=100),
        ),
    ]