# Generated by Django 5.0.1 on 2024-01-25 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_email', '0003_remove_useremail_title_useremail_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='useremail',
            name='title',
            field=models.CharField(choices=[('1', 'Mrs'), ('2', 'Mr'), ('3', 'Ms'), ('4', 'Miss'), ('5', 'Dr')], default='Mr', max_length=1),
        ),
        migrations.AlterField(
            model_name='useremail',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=''),
        ),
    ]
