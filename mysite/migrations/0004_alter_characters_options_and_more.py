# Generated by Django 5.2 on 2025-04-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_alter_characters_options_characters_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characters',
            options={'ordering': ['active']},
        ),
        migrations.RenameField(
            model_name='characters',
            old_name='right_cnt',
            new_name='pinyin_right_cnt',
        ),
        migrations.AddField(
            model_name='characters',
            name='translation_right_cnt',
            field=models.IntegerField(default=0),
        ),
    ]
