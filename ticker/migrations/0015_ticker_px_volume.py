# Generated by Django 4.0.6 on 2022-07-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0014_ticker_px_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='px_volume',
            field=models.BigIntegerField(null=True, verbose_name='px_volume'),
        ),
    ]
