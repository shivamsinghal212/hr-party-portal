# Generated by Django 3.1.2 on 2020-10-10 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('platform', models.PositiveSmallIntegerField(null=True)),
                ('soft_delete', models.PositiveSmallIntegerField(default=0)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('status', models.SmallIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('platform', models.PositiveSmallIntegerField(null=True)),
                ('soft_delete', models.PositiveSmallIntegerField(default=0)),
                ('status', models.SmallIntegerField(default=1)),
                ('description', models.CharField(max_length=50)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='party.party')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]