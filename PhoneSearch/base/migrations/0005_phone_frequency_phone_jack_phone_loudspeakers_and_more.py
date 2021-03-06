# Generated by Django 4.0 on 2022-01-17 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_phone_mainfeatures_alter_phone_dual'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='frequency',
            field=models.CharField(blank=True, max_length=200, verbose_name='Sound Frequency'),
        ),
        migrations.AddField(
            model_name='phone',
            name='jack',
            field=models.CharField(blank=True, max_length=200, verbose_name='3.5mm jack'),
        ),
        migrations.AddField(
            model_name='phone',
            name='loudspeakerS',
            field=models.CharField(blank=True, max_length=200, verbose_name='Loudspeaker'),
        ),
        migrations.AddField(
            model_name='phone',
            name='sound',
            field=models.CharField(default='SOUND', max_length=200, verbose_name='Sound'),
        ),
    ]
