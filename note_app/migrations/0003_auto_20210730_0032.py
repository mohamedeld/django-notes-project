# Generated by Django 2.1.5 on 2021-07-29 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note_app', '0002_note_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='image',
            new_name='img',
        ),
    ]
