# Generated by Django 5.0.7 on 2024-07-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0007_country_alter_address_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
