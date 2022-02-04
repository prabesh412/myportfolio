# Generated by Django 4.0.1 on 2022-01-28 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_customer_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='customers',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='customer',
        ),
        migrations.DeleteModel(
            name='order',
        ),
        migrations.DeleteModel(
            name='orderitem',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecom.category'),
        ),
    ]
