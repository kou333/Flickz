# Generated by Django 3.1 on 2020-08-31 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0002_auto_20200831_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='booked_time',
            field=models.TimeField(default='20:00:16', editable=False, max_length=250),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='booking_time',
            field=models.IntegerField(default=1598884216, editable=False),
        ),
    ]
