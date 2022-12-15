# Generated by Django 4.1.4 on 2022-12-10 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Register",
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
                ("f1name", models.CharField(max_length=200)),
                ("lname", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=200)),
                ("location", models.CharField(max_length=200)),
                ("zip", models.CharField(max_length=200)),
                ("sgrade", models.CharField(max_length=200)),
                ("ssubject", models.CharField(max_length=200)),
                ("why", models.CharField(max_length=2000)),

            ],
        ),
    ]
