# Generated by Django 3.0.14 on 2025-01-15 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20250115_1009'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('title', 'lat', 'lng')},
        ),
    ]
