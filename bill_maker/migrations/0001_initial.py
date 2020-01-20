# Generated by Django 2.2.3 on 2019-12-19 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('starters', 'STARTERS'), ('mains', 'MAINS'), ('desserts', 'DESSERTS'), ('drinks', 'DRINKS')], default='starters', max_length=15)),
                ('name', models.CharField(default='', max_length=500, unique=True)),
                ('price', models.FloatField()),
                ('short_description', models.CharField(default='', max_length=100)),
            ],
        ),
    ]