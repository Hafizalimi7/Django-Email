# Generated by Django 5.0.1 on 2024-01-24 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_email', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremail',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]