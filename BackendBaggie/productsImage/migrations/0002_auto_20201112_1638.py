# Generated by Django 3.1.1 on 2020-11-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsImage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='imageName',
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload_products'),
        ),
    ]
