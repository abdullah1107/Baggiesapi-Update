# Generated by Django 3.1.1 on 2020-11-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20201112_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderTrakingNumber',
            field=models.CharField(blank=True, default='8573132307', editable=False, max_length=10, unique=True),
        ),
    ]
