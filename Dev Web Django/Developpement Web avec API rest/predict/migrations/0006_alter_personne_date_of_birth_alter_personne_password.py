# Generated by Django 4.2.1 on 2023-06-03 22:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0005_alter_personne_options_alter_personne_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personne",
            name="date_of_birth",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 3, 22, 57, 16, 81413)
            ),
        ),
        migrations.AlterField(
            model_name="personne",
            name="password",
            field=models.CharField(max_length=12000),
        ),
    ]
