# Generated by Django 5.0.6 on 2024-06-17 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_rename_email_address_subscribe_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='Aboutevent',
            new_name='aboutevent',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='Banner',
            new_name='banner',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='Desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='End_date',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='End_time',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='Eventname',
            new_name='eventname',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='Eventurl',
            new_name='eventurl',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='Imp',
            new_name='imp',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='Start_date',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='Start_time',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='Venue',
            new_name='venue',
        ),
        migrations.AlterModelTable(
            name='events',
            table='events',
        ),
    ]
