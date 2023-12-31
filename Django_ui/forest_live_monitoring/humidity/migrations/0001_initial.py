# Generated by Django 4.1.3 on 2023-10-13 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sensors',
            fields=[
                ('Node_id', models.AutoField(primary_key=True, serialize=False)),
                ('Latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('Longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
            options={
                'db_table': 'sensors',
                'unique_together': {('Latitude', 'Longitude')},
            },
        ),
        migrations.CreateModel(
            name='sensorReadings',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Temperature', models.FloatField()),
                ('Humidity', models.FloatField()),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('Node_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='humidity.sensors')),
            ],
            options={
                'db_table': 'sensorReadings',
                'unique_together': {('ID', 'Node_id')},
            },
        ),
    ]
