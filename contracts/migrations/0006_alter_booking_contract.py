# Generated by Django 5.0.1 on 2024-03-06 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0005_alter_contract_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='contract',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contracts.contract'),
        ),
    ]