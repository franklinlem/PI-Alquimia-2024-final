# Generated by Django 5.0.6 on 2024-05-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.BigIntegerField(default=0),
        ),
    ]