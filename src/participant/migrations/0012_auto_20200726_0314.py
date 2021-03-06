# Generated by Django 3.0.8 on 2020-07-26 01:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0011_auto_20200726_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='This is not a valid phone number.', regex='0[567][0-9]{8}')]),
        ),
    ]
