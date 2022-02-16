# Generated by Django 4.0.1 on 2022-02-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
