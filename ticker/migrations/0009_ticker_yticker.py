# Generated by Django 4.0.6 on 2022-07-27 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0008_remove_ticker_date_remove_ticker_px_high_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='yticker',
            field=models.CharField(db_index=True, default='_', max_length=12, verbose_name='yticker'),
        ),
    ]
