# Generated by Django 5.0.1 on 2024-01-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_email', '0004_useremail_title_alter_useremail_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremail',
            name='body',
            field=models.EmailField(max_length=1000),
        ),
    ]
