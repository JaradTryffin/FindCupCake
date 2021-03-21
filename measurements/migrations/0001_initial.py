# Generated by Django 3.0.3 on 2021-03-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_point', models.CharField(blank=True, max_length=200, null=True)),
                ('end_point', models.CharField(max_length=200)),
                ('type_of_transport', models.CharField(choices=[('car', 'Car'), ('train', 'Train'), ('PLANE', 'Plane'), ('bus', 'Bus')], max_length=30)),
                ('price_per_km', models.FloatField()),
                ('price_per_hour', models.FloatField()),
                ('distance', models.FloatField()),
                ('cost', models.FloatField()),
                ('time', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]