# Generated by Django 3.1.5 on 2021-01-12 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('cost_price', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=200)),
                ('selling_price', models.IntegerField(default=0)),
                ('pub_date', models.DateField(default=datetime.date.today)),
                ('barcode', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
