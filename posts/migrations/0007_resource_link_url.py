# Generated by Django 4.2.11 on 2024-04-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_resource_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='link_url',
            field=models.URLField(blank=True),
        ),
    ]
