# Generated by Django 2.1.1 on 2018-09-14 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0002_auto_20180914_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='court',
            old_name='coordinate_x',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='court',
            old_name='coordinate_y',
            new_name='lng',
        ),
    ]