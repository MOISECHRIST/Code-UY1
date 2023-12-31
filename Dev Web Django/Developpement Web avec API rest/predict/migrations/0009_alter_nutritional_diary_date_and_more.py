# Generated by Django 4.2.1 on 2023-06-03 23:14

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0008_alter_personne_date_of_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nutritional_diary",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="personne",
            name="date_of_birth",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 3, 23, 14, 52, 128687, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
