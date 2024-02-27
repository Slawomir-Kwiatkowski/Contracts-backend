# Generated by Django 5.0.1 on 2024-02-28 19:58

import contracts.models.contract
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_alter_contract_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contractor',
            field=models.CharField(choices=contracts.models.contract.Contract.contractors_choices, max_length=15),
        ),
    ]