# Generated by Django 4.2 on 2024-05-17 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0006_alter_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deliver_time', models.DateTimeField()),
                ('quantity', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('factor', models.FileField(upload_to='factor/')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ResponseOrder',
                'verbose_name_plural': 'ResponseOrders',
            },
        ),
    ]
