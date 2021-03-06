# Generated by Django 2.1.2 on 2018-11-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20181117_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('0', 'FAILED'), ('1', 'PLACED'), ('2', 'CONFIRMED'), ('3', 'OUT FOR DELIVERY'), ('4', 'DELIVERED')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.CharField(choices=[('1', 'COD'), ('2', 'ONLINE')], default='1', max_length=1),
        ),
    ]
