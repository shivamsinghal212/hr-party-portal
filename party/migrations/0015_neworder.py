# Generated by Django 3.1.2 on 2020-10-11 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('party', '0014_auto_20201011_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(1, 'OPEN'), (0, 'CLOSED')], default=1)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='party', chained_model_field='party', on_delete=django.db.models.deletion.CASCADE, to='party.menuitems')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='party.party')),
            ],
            options={
                'verbose_name_plural': 'New Orders',
                'unique_together': {('employee', 'party')},
            },
        ),
    ]