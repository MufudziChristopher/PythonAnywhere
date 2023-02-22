# Generated by Django 3.0.8 on 2020-08-04 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Axis', '0010_auto_20200804_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Order Status',
                'verbose_name_plural': 'Order Statuses',
            },
        ),
        migrations.RemoveField(
            model_name='order',
            name='complete',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]