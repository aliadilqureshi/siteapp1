# Generated by Django 3.0.7 on 2020-07-16 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='saf_defect_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saf_number_in_table', models.FloatField()),
                ('defect_number_in_table', models.FloatField()),
            ],
        ),
    ]
