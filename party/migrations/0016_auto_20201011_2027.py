# Generated by Django 3.1.2 on 2020-10-11 20:27

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0015_neworder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='party',
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='item',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='order', chained_model_field='party', on_delete=django.db.models.deletion.CASCADE, to='party.menuitems'),
        ),
    ]