# Generated by Django 5.0 on 2023-12-14 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_image_mobile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='phone_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
