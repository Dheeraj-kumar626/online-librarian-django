# Generated by Django 2.0 on 2018-04-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libr', '0008_auto_20180408_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='NoofContrib',
            field=models.IntegerField(default=0),
        ),
    ]
