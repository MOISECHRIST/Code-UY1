# Generated by Django 4.2.1 on 2023-06-03 23:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0007_alter_personne_date_of_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personne",
            name="date_of_birth",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 3, 23, 13, 45, 67811, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]