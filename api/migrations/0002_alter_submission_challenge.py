# Generated by Django 5.1.6 on 2025-02-26 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='challenge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='submissions', to='api.challenge'),
        ),
    ]
