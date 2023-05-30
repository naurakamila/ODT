# Generated by Django 4.1.8 on 2023-05-13 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pemasukan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('jumlah', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tanggal', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pengeluaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('jumlah', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tanggal', models.DateField()),
            ],
        ),
    ]
