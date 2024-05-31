# Generated by Django 5.0.6 on 2024-05-31 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_rename_work_place_redikt_work_place_uz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='description_en',
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description_uz',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
