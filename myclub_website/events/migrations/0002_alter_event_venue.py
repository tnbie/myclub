# Generated by Django 4.0.4 on 2022-05-07 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue'),
        ),
    ]
