# Generated by Django 4.2 on 2024-04-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('author', models.CharField(max_length=200)),
                ('checked_out', models.BooleanField()),
                ('checkout_date', models.DateField()),
            ],
        ),
    ]
