# Generated by Django 4.2.1 on 2023-06-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="personne",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="user_img"),
        ),
        migrations.AlterField(
            model_name="food",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="food_img"),
        ),
    ]
