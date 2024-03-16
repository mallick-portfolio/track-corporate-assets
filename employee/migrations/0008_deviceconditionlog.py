# Generated by Django 5.0.3 on 2024-03-16 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_rename_assigndevice_allocationdevice'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceConditionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.device')),
            ],
        ),
    ]
