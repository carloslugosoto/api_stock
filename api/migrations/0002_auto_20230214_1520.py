# Generated by Django 3.2.15 on 2023-02-14 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='location',
        ),
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.location'),
            preserve_default=False,
        ),
    ]
