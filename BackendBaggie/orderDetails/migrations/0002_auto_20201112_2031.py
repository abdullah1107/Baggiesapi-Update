# Generated by Django 3.1.1 on 2020-11-12 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20201112_2031'),
        ('orderDetails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='oderID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='orders.order'),
        ),
    ]
