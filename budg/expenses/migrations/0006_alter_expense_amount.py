# Generated by Django 4.1.1 on 2022-12-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_remove_expense_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
