# Generated by Django 4.0.6 on 2022-07-27 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0012_ticker_px_high'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='px_low',
            field=models.FloatField(null=True, verbose_name='px_low'),
        ),
    ]