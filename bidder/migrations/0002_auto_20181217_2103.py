# Generated by Django 2.1.3 on 2018-12-17 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address_line_two',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='district',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='post_code',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
