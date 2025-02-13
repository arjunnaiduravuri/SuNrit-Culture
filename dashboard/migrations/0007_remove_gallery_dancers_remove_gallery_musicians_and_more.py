# Generated by Django 5.0.6 on 2024-06-10 03:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_gallery_dancers_alter_gallery_musicians'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='Dancers',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='Musicians',
        ),
        migrations.CreateModel(
            name='Dancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='dancers/')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dancers', to='dashboard.gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='musicians/')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musicians', to='dashboard.gallery')),
            ],
        ),
    ]
