# Generated by Django 4.1.2 on 2022-10-26 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='time',
        ),
    ]