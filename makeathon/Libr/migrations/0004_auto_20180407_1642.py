# Generated by Django 2.0 on 2018-04-07 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Libr', '0003_auto_20180407_1619'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('callno', 'accno')},
        ),
    ]
