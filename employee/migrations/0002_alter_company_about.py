# Generated by Django 5.0.3 on 2024-03-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
