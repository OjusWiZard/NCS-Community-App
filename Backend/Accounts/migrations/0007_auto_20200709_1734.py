# Generated by Django 3.0.8 on 2020-07-09 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_auto_20200708_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('portfolio', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('kaggle', models.URLField(blank=True, null=True)),
                ('codechef', models.URLField(blank=True, null=True)),
                ('codeforces', models.URLField(blank=True, null=True)),
                ('hackerrank', models.URLField(blank=True, null=True)),
                ('hackerearth', models.URLField(blank=True, null=True)),
                ('topcoder', models.URLField(blank=True, null=True)),
                ('codewars', models.URLField(blank=True, null=True)),
                ('leetcode', models.URLField(blank=True, null=True)),
                ('spoj', models.URLField(blank=True, null=True)),
                ('codeingame', models.URLField(blank=True, null=True)),
                ('behance', models.URLField(blank=True, null=True)),
                ('medium', models.URLField(blank=True, null=True)),
                ('fossbyte', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_links',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.User_links'),
        ),
    ]
