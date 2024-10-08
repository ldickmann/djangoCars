# Generated by Django 5.1 on 2024-08-25 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='gearshift',
            field=models.CharField(blank=True, choices=[('manual', 'Manual'), ('automatic', 'Automatic'), ('cvt', 'CVT')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
