# Generated by Django 5.0.6 on 2024-05-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vitrine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('produto_id', models.PositiveIntegerField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]
