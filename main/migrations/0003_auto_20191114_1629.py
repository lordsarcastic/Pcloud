# Generated by Django 2.2.5 on 2019-11-14 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191113_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='path',
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='drive',
            name='cover_picture',
            field=models.ImageField(default='media/drive.png', upload_to='media/<function user_path at 0x7ff088828048>'),
        ),
        migrations.AlterField(
            model_name='file',
            name='cover_picture',
            field=models.ImageField(default='media/file.png', upload_to='media/<function user_path at 0x7ff088828048>'),
        ),
        migrations.AlterField(
            model_name='file',
            name='item',
            field=models.FileField(upload_to='media/<function user_path at 0x7ff088828048>'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='cover_picture',
            field=models.ImageField(default='media/folder-white.png', upload_to='media/<function user_path at 0x7ff088828048>'),
        ),
    ]