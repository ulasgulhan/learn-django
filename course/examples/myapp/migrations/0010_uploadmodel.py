# Generated by Django 4.2.7 on 2023-12-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_address_supplier_product_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images')),
            ],
        ),
    ]
