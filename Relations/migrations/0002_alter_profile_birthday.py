# Generated by Django 4.0.1 on 2022-01-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Relations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
