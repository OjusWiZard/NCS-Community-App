# Generated by Django 3.0.8 on 2020-07-13 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nibblites', '0003_auto_20200712_0237'),
        ('Accounts', '0010_auto_20200712_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='techstack',
        ),
        migrations.AddField(
            model_name='user',
            name='techstack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='Nibblites.TechStack'),
        ),
    ]
