# Generated by Django 3.1.13 on 2021-11-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211129_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='geometry',
            field=models.TextField(),
        ),
    ]
