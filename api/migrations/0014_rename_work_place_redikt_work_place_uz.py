# Generated by Django 5.0.6 on 2024-05-30 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_redikt_work_place_en_redikt_work_place_ru'),
    ]

    operations = [
        migrations.RenameField(
            model_name='redikt',
            old_name='work_place',
            new_name='work_place_uz',
        ),
    ]
