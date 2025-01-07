# Generated by Django 3.0.14 on 2025-01-07 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('lng', models.DecimalField(decimal_places=14, max_digits=16)),
                ('lat', models.DecimalField(decimal_places=14, max_digits=16)),
            ],
        ),
    ]
