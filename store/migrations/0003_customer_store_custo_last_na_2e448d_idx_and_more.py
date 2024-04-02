# Generated by Django 5.0.3 on 2024-04-02 13:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_add_slug_to_product"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="customer",
            index=models.Index(
                fields=["last_name", "first_name"],
                name="store_custo_last_na_2e448d_idx",
            ),
        ),
        migrations.AlterModelTable(
            name="customer",
            table="store_customer",
        ),
    ]
