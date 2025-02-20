# Generated by Django 4.2.18 on 2025-01-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Build_Board', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='max_otp_try',
            field=models.CharField(default=3, max_length=2),
        ),
        migrations.AddField(
            model_name='customer',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='otp_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='otp_max_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
