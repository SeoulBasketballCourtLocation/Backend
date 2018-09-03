# Generated by Django 2.1.1 on 2018-09-03 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('coordinate_x', models.CharField(max_length=255)),
                ('coordinate_y', models.CharField(max_length=255)),
                ('no_basket', models.IntegerField()),
                ('bench', models.BooleanField(default=False)),
                ('showerbox', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
            ],
        ),
    ]
