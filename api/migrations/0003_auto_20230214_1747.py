# Generated by Django 3.2.15 on 2023-02-14 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230214_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='location',
        ),
        migrations.AddField(
            model_name='stock',
            name='location',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='api.location'),
            preserve_default=False,
        ),
    ]
