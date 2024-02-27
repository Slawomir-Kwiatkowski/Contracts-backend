# Generated by Django 5.0.1 on 2024-03-04 21:20

import contracts.models.contract
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_alter_contract_contractor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='warehouse',
            field=models.CharField(choices=contracts.models.contract.Contract.warehouses_choices, max_length=15),
        ),
    ]