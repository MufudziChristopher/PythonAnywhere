# Generated by Django 4.1.7 on 2023-03-04 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Marz", "0002_rename_name_product_name1_product_name2"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image5",
            field=models.ImageField(blank=True, upload_to="main_product/"),
        ),
    ]
