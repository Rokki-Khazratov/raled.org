# Generated by Django 5.0.6 on 2024-05-22 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_social_media_product_doi'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='best',
            field=models.BooleanField(default=False),
        ),
    ]