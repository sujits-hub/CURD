# Generated by Django 3.0.5 on 2020-05-07 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entery',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('data1', models.CharField(max_length=50)),
                ('data2', models.CharField(max_length=50)),
            ],
        ),
    ]
