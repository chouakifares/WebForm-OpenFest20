# Generated by Django 3.0.8 on 2020-07-26 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0010_auto_20200726_0226'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='participant',
            name='unique name',
        ),
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together={('first_name', 'last_name')},
        ),
    ]
