# Generated by Django 4.0 on 2021-12-16 12:25

import categories.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("expenses", "0004_auto_20211216_1218"),
    ]

    state_operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", categories.models.LCharField(max_length=50)),
                ("color", models.CharField(default="#000000", max_length=7)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="accounts.user",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Categories",
                "unique_together": {("name", "owner")},
                "db_table": "categories_category",
            },
            bases=(models.Model,),
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]