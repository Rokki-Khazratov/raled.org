# Generated by Django 5.0.2 on 2024-10-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_bookorder_delete_partner_delete_worker_member_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
