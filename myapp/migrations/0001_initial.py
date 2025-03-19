# Generated by Django 5.1.7 on 2025-03-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=50)),
                ('is_group', models.BooleanField(default=False)),
                ('members', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
