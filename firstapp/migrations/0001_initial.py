# Generated by Django 2.0.6 on 2019-09-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(default='', max_length=200)),
                ('userPassword', models.BigIntegerField()),
                ('userEmail', models.CharField(default='', max_length=200)),
                ('userImage', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
