# Generated by Django 5.0.7 on 2024-08-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_alter_tweet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tweet_images/'),
        ),
    ]
