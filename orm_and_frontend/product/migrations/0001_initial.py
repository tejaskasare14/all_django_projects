# Generated by Django 4.2.6 on 2024-01-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('details', models.CharField(max_length=150)),
                ('category', models.IntegerField()),
                ('is_active', models.BooleanField()),
                ('rating', models.FloatField()),
            ],
        ),
    ]
