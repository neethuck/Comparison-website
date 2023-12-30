# Generated by Django 5.0 on 2023-12-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_mobile_internal_storage_mobile_ram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='battery_capacity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='display_size',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='image',
            field=models.ImageField(upload_to='mobile_images'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='internal_storage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='ram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]