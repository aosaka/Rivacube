# Generated by Django 4.0.6 on 2022-08-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0017_alter_lexique_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lexique',
            name='sector',
            field=models.CharField(max_length=32, verbose_name='sector'),
        ),
    ]
