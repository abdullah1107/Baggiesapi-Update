# Generated by Django 3.1.1 on 2020-11-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20201113_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderTrakingNumber',
            field=models.CharField(blank=True, default='3685085935', editable=False, max_length=10, unique=True),
        ),
    ]
