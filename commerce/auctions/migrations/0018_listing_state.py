# Generated by Django 4.0.6 on 2022-07-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_listing_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(default='active', max_length=10),
            preserve_default=False,
        ),
    ]
