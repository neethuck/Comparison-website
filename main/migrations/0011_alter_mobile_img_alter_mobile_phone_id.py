# Generated by Django 5.0 on 2023-12-14 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_mobile_phone_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='Img',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='phone_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]