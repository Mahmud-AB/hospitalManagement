# Generated by Django 4.1.1 on 2022-09-28 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("p_name", models.CharField(blank=True, max_length=200, null=True)),
                ("email", models.EmailField(blank=True, max_length=200, null=True)),
                ("d_name", models.CharField(blank=True, max_length=200, null=True)),
                ("speciality", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "phoneNumber",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
        ),
    ]
