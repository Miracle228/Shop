# Generated by Django 2.2.2 on 2019-06-26 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_remove_articels_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='articels',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]