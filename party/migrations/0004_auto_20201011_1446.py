# Generated by Django 3.1.2 on 2020-10-11 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0003_auto_20201011_1431'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='menuitems',
            unique_together={('party', 'description')},
        ),
    ]
