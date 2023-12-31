# Generated by Django 4.2.4 on 2023-11-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BuyTransaction",
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
                ("date", models.DateField()),
                ("company", models.CharField(max_length=255)),
                ("trade_type", models.CharField(default="BUY", max_length=4)),
                ("quantity", models.PositiveIntegerField()),
                (
                    "price_per_share",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SellTransaction",
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
                ("date", models.DateField()),
                ("company", models.CharField(max_length=255)),
                ("trade_type", models.CharField(default="SELL", max_length=4)),
                ("quantity", models.PositiveIntegerField()),
                (
                    "price_per_share",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SplitTransaction",
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
                ("date", models.DateField()),
                ("company", models.CharField(max_length=255)),
                ("trade_type", models.CharField(default="SPLIT", max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
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
                ("company", models.CharField(max_length=255, unique=True)),
                ("quantity", models.PositiveIntegerField(default=0)),
                (
                    "average_buy_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
            ],
        ),
    ]
