# Generated by Django 3.0.6 on 2021-03-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256)),
                ('sysmbol', models.CharField(blank=True, max_length=256)),
                ('industry', models.CharField(blank=True, max_length=256)),
                ('isinCode', models.CharField(blank=True, max_length=256)),
            ],
        ),
    ]