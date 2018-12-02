# Generated by Django 2.1.3 on 2018-12-02 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_amount', models.IntegerField()),
                ('bid_notes', models.CharField(max_length=100)),
                ('messages', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='BookingRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_time', models.DateTimeField()),
                ('pickup_landmark', models.CharField(max_length=100)),
                ('estimated_distance', models.IntegerField()),
                ('number_of_passengers', models.IntegerField()),
                ('number_of_large_bags', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('address_line_one', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('party_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bidder.Party')),
                ('identity_proof', models.CharField(max_length=100)),
                ('payment_method', models.CharField(max_length=100)),
                ('fav_locations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidder.Location')),
            ],
            bases=('bidder.party',),
        ),
        migrations.CreateModel(
            name='ServiceProvier',
            fields=[
                ('party_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bidder.Party')),
                ('license_details', models.CharField(max_length=100)),
                ('payment_details', models.CharField(max_length=100)),
                ('insurance', models.CharField(max_length=100)),
                ('service_geo_coverage', models.CharField(max_length=100)),
            ],
            bases=('bidder.party',),
        ),
        migrations.AddField(
            model_name='party',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidder.Location'),
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='dropoff_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_to', to='bidder.Location'),
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='pickup_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_from', to='bidder.Location'),
        ),
        migrations.AddField(
            model_name='bid',
            name='bid_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidder.ServiceProvier'),
        ),
    ]
