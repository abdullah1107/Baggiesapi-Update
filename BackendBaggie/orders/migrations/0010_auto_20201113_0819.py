# Generated by Django 3.1.1 on 2020-11-13 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20201113_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderTrakingNumber',
            field=models.CharField(blank=True, default='2612670009', editable=False, max_length=10, unique=True),
        ),
    ]
