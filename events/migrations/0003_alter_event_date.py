# Generated by Django 4.0.9 on 2023-04-10 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_options_alter_event_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(verbose_name='تاریخ'),
        ),
    ]