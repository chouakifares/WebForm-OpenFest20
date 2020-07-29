# Generated by Django 3.0.8 on 2020-07-26 00:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0004_auto_20200726_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='branch',
            field=models.CharField(choices=[('MI', 'Mathematique et Informatique'), ('SM', 'Science de la Matière'), ('ST', 'Science et Technologie'), ('SNV', 'Science de la Nature et de la Vie'), ('STU', "Science de la Terre et de l'Univers"), ('Mathematique', 'Mathematique'), ('FEI', 'Electronique et Informatique'), ('Physique', 'Physique'), ('Chimie', 'Chimie'), ('GC', 'Génie Civile'), ('GM', 'Génie Mecanique'), ('GP', 'Génie des Procédés'), ('Bio', 'Biologie'), ('Science de la Terre', 'Science de la Terre'), ('GAT', 'Géographie et Amenagement du Territoire'), ('O', 'Other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_first_name', message='This is not a valid first name.', regex="^[a-zA-Z]+(([\\'\\,\\.\\- ][a-zA-Z ])?[a-zA-Z]*)*$")]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(code='invalid_last_name', message='This is not a valid last name.', regex="^[a-zA-Z]+(([\\'\\,\\.\\- ][a-zA-Z ])?[a-zA-Z]*)*$")]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='level',
            field=models.CharField(choices=[('L1', 'License 1'), ('L2', 'License 2'), ('L3', 'License 3'), ('M1', 'Master 1'), ('M2', 'Master 2'), ('D', 'Doctorat'), ('O', 'Other')], max_length=5),
        ),
        migrations.AlterField(
            model_name='participant',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='participant',
            name='university',
            field=models.CharField(choices=[('USTHB', 'USTHB'), ('ENP', 'ENP'), ('ENSTP', 'ENSTP'), ('ESI', 'ESI'), ('ESSA', 'ESSA'), ('O', 'Other')], max_length=5),
        ),
    ]