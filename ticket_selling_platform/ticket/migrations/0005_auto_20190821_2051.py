# Generated by Django 2.2.4 on 2019-08-21 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_auto_20190821_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='seat_number',
        ),
        migrations.AddField(
            model_name='ticket',
            name='seat_identifier',
            field=models.CharField(default='R1', max_length=10),
            preserve_default=False,
        ),
    ]
