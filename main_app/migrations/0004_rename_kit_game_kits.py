# Generated by Django 4.0.4 on 2022-04-27 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_kit_alter_winner_options_game_kit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='kit',
            new_name='kits',
        ),
    ]
