# Generated by Django 5.1.7 on 2025-03-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expense',
            name='members',
            field=models.TextField(blank=True, null=True),
        ),
    ]
