# Generated by Django 5.0.6 on 2024-06-17 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_rename_aboutevent_events_aboutevent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='aboutevent',
            new_name='Aboutevent',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='banner',
            new_name='Banner',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='category',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='desc',
            new_name='Desc',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='end_date',
            new_name='End_date',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='end_time',
            new_name='End_time',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='eventname',
            new_name='Eventname',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='eventurl',
            new_name='Eventurl',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='imp',
            new_name='Imp',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='start_date',
            new_name='Start_date',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='start_time',
            new_name='Start_time',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='venue',
            new_name='Venue',
        ),
    ]
