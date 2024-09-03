# Generated by Django 5.0.6 on 2024-06-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]