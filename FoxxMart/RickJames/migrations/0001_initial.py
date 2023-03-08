# Generated by Django 4.1.7 on 2023-03-08 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RickJamesCustomer",
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
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "email",
                    models.EmailField(
                        max_length=60, null=True, unique=True, verbose_name="email"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RickJamesOrder",
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
                ("date_ordered", models.DateTimeField(auto_now_add=True)),
                ("transaction_id", models.CharField(max_length=200, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            (
                                "Payment Confirmed, Processing Order",
                                "Payment Confirmed, Processing Order",
                            ),
                            ("Out for delivery", "Out for delivery"),
                            ("Delivered", "Delivered"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="RickJames.rickjamescustomer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RickJamesProduct",
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
                ("name1", models.CharField(max_length=200)),
                ("name2", models.CharField(max_length=200)),
                ("description1", models.TextField(max_length=2000)),
                ("description2", models.TextField(max_length=2000)),
                (
                    "image1",
                    models.ImageField(blank=True, upload_to="RickJames_product/"),
                ),
                (
                    "image2",
                    models.ImageField(blank=True, upload_to="RickJames_product/"),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stock", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="RickJamesShippingAddress",
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
                ("country", models.CharField(max_length=200)),
                ("address1", models.CharField(max_length=200)),
                ("address2", models.CharField(max_length=200, null=True)),
                ("suburb", models.CharField(max_length=200, null=True)),
                ("city", models.CharField(max_length=200)),
                ("province", models.CharField(max_length=200)),
                ("postal_code", models.CharField(max_length=20)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="RickJamesOrderItem",
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
                ("quantity", models.IntegerField(blank=True, default=0, null=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="RickJames.rickjamesorder",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="RickJames.rickjamesproduct",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="rickjamescustomer",
            name="shippingAddress",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="RickJames.rickjamesshippingaddress",
            ),
        ),
        migrations.AddField(
            model_name="rickjamescustomer",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
