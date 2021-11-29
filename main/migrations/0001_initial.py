# Generated by Django 3.1.13 on 2021-11-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PLNT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SEQPLT19', models.IntegerField()),
                ('PSTATABB', models.CharField(max_length=10)),
                ('PNAME', models.CharField(max_length=100)),
                ('LAT', models.CharField(max_length=20)),
                ('LON', models.CharField(max_length=20)),
                ('PLNGENAN', models.FloatField()),
            ],
        ),
    ]