# Generated by Django 5.0.4 on 2024-04-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masseges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anser',
            name='anser',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=100),
        ),
    ]