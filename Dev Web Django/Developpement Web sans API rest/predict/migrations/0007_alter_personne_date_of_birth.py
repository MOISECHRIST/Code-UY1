# Generated by Django 4.2.1 on 2023-06-03 23:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0006_alter_personne_date_of_birth_alter_personne_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personne",
            name="date_of_birth",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 3, 23, 12, 51, 182943)
            ),
        ),
    ]