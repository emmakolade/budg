# Generated by Django 4.1.3 on 2022-12-09 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_expense_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='updated',
        ),
    ]
