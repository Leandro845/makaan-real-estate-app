# Generated by Django 5.0.6 on 2024-06-17 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_client_user_image'),
        ('property', '0007_alter_property_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.client'),
        ),
    ]
