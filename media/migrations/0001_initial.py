# Generated by Django 4.0.6 on 2022-08-11 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('status_id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='status_id')),
                ('user_id', models.BigIntegerField(verbose_name='user_id')),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
                ('screen_name', models.CharField(max_length=32, verbose_name='screen_name')),
                ('text', models.TextField(verbose_name='text')),
                ('source', models.CharField(max_length=32, verbose_name='source')),
                ('display_text_width', models.SmallIntegerField(verbose_name='display_text_width')),
                ('reply_to_user_id', models.BigIntegerField(verbose_name='replay_to_user_id')),
                ('reply_to_screen_name', models.CharField(max_length=32, verbose_name='reply_to_screen_name')),
                ('is_quote', models.BooleanField(verbose_name='is_quote')),
                ('is_retweet', models.BooleanField(verbose_name='is_retweet')),
                ('favorite_count', models.SmallIntegerField(verbose_name='favorite_count')),
                ('retweet_count', models.SmallIntegerField(verbose_name='retweet_count')),
                ('mentions_screen_name', models.CharField(max_length=32, verbose_name='mentions_screen_name')),
                ('lang', models.CharField(max_length=3, verbose_name='lang')),
                ('description', models.TextField(verbose_name='description')),
                ('reply_to_status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.media')),
            ],
        ),
    ]
