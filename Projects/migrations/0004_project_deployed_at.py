# Generated by Django 3.0.8 on 2020-07-09 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0003_auto_20200709_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deployed_at',
            field=models.URLField(blank=True, null=True),
        ),
    ]