# Generated by Django 4.2.2 on 2023-06-08 08:45

from django.db import migrations, models
import django.db.models.deletion
import patients.utils


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GenderTable",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=patients.utils.get_uuid,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("MALE", "Male"),
                            ("FEMALE", "Female"),
                            ("OTHERS", "Others"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ServicesTable",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=patients.utils.get_uuid,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("service_name", models.CharField(max_length=50)),
                ("service_price", models.PositiveBigIntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PatientTable",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=patients.utils.get_uuid,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("patient_name", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=50)),
                ("dob", models.DateField()),
                (
                    "gender",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patients.gendertable",
                    ),
                ),
                (
                    "service",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patients.servicestable",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
