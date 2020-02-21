# Generated by Django 3.0.3 on 2020-02-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0008_auto_20200210_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vat', models.BooleanField(default=True, verbose_name='Vat note')),
                ('price_valid', models.BooleanField(default=False, verbose_name='Price validity')),
                ('price_birr', models.BooleanField(default=False, verbose_name='Price in Birr')),
                ('delivery', models.BooleanField(default=False, verbose_name='Delivery')),
                ('payment_term', models.BooleanField(default=False, verbose_name='Payment term')),
                ('installation', models.BooleanField(default=False, verbose_name='Installation')),
                ('discrepancy', models.BooleanField(default=False, verbose_name='Price discrepancy')),
            ],
        ),
    ]
