# Generated by Django 3.1.1 on 2020-11-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_auto_20201115_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderTrakingNumber',
            field=models.CharField(blank=True, default='8696526433', editable=False, max_length=10, unique=True),
        ),
    ]
