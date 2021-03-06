# Generated by Django 3.2.12 on 2022-05-26 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('mode', models.CharField(choices=[('solar', 'PV'), ('wind', 'WT')], default='solar', max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'site',
                'ordering': ['value'],
            },
        ),
        migrations.DeleteModel(
            name='Sites',
        ),
    ]
