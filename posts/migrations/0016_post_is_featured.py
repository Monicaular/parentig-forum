# Generated by Django 4.2.11 on 2024-04-30 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_rule'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
