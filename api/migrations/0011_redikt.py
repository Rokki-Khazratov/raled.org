# Generated by Django 5.0.6 on 2024-05-30 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_rename_fup_regulation_about_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redikt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('work_place', models.TextField()),
                ('discription', models.TextField()),
            ],
        ),
    ]
