# Generated by Django 4.0 on 2022-01-17 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_bio_user_name_alter_user_email_phonename_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='fivegBands',
            field=models.CharField(blank=True, max_length=200, verbose_name='5G bands'),
        ),
    ]
