# Generated by Django 4.1.2 on 2022-11-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookable1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booked_community_hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=500)),
                ('phn_no', models.CharField(max_length=500)),
                ('eid', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=750)),
                ('dateb', models.DateField(unique=True)),
                ('vname', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='booked_garden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=500)),
                ('phn_no', models.CharField(max_length=500)),
                ('eid', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=750)),
                ('dateb', models.DateField(unique=True)),
                ('vname', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='booked_pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=500)),
                ('phn_no', models.CharField(max_length=500)),
                ('eid', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=750)),
                ('dateb', models.DateField(unique=True)),
                ('vname', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='booked_venues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=500)),
                ('phn_no', models.CharField(max_length=500)),
                ('eid', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=750)),
                ('dateb', models.DateField(unique=True)),
                ('vname', models.CharField(max_length=500)),
            ],
        ),
        migrations.RenameModel(
            old_name='booked',
            new_name='booked_hall',
        ),
    ]
