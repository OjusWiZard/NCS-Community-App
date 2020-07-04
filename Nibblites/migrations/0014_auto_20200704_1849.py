# Generated by Django 3.0.8 on 2020-07-04 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nibblites', '0013_auto_20200704_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nibblites.Branch', to_field='branch_code'),
        ),
        migrations.AlterField(
            model_name='user',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nibblites.Club', to_field='club'),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nibblites.Designation', to_field='designation'),
        ),
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nibblites.Year', to_field='year'),
        ),
    ]
