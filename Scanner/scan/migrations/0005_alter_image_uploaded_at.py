# Generated by Django 4.0.3 on 2024-07-18 18:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0004_user_address_user_age_alter_image_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 18, 18, 30, 2, 880809, tzinfo=utc)),
        ),
    ]