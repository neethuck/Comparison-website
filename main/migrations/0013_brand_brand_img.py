# Generated by Django 5.0 on 2023-12-26 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_delete_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_img',
            field=models.ImageField(blank=True, null=True, upload_to='brand'),
        ),
    ]
