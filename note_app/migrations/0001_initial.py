# Generated by Django 2.0.3 on 2021-07-29 19:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('content', models.TextField(blank=True, max_length=255)),
                ('last_update', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('active', models.BooleanField(default=True)),
                ('tags', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
