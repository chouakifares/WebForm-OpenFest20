# Generated by Django 3.0.8 on 2020-07-26 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0016_auto_20200726_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='branch',
            field=models.CharField(choices=[('', 'Select Your Branch'), ('MI', 'Mathematics and Computer Science'), ('SM', 'Science of Matter'), ('ST', 'Science and Technology'), ('SNV', 'Science of Nature and Life'), ('STU', 'Science of Earth and the Universe'), ('MATH', 'Mathematics'), ('FEI', 'Electric Engineering and Computer Science'), ('PHY', 'Physics'), ('CHI', 'Chemistry'), ('GC', 'Civil Engineering'), ('GM', 'Mechanical Engineering'), ('GP', 'Process Engineering'), ('BIO', 'Biology'), ('EARTH', 'Science of Earth'), ('GAT', 'Geography and Territorial Planning'), ('O', 'Other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='level',
            field=models.CharField(choices=[('', 'Select Your Level'), ('L1', 'Undergrad. deg. 1'), ('L2', 'Undergrad. deg. 2'), ('L3', 'Undergrad. deg.3'), ('M1', "Master's deg. 1"), ('M2', "Master's deg. 2"), ('D', 'Doctorate deg.'), ('O', 'Other')], max_length=5),
        ),
    ]
