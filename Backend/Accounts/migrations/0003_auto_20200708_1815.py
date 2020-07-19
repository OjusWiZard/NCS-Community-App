# Generated by Django 3.0.8 on 2020-07-08 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_auto_20200708_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Branch', to_field='branch_code'),
        ),
        migrations.AlterField(
            model_name='user',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Club', to_field='club'),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Designation', to_field='designation'),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Session'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Year', to_field='year'),
        ),
    ]
