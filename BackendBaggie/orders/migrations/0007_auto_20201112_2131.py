# Generated by Django 3.1.1 on 2020-11-12 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20201112_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderTrakingNumber',
            field=models.CharField(blank=True, default='7631487466', editable=False, max_length=10, unique=True),
        ),
    ]
