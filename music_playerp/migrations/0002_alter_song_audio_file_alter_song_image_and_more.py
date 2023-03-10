# Generated by Django 4.1.5 on 2023-01-29 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_playerp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/music/song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/music/song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
