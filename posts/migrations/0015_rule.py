# Generated by Django 4.2.11 on 2024-04-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_alter_comment_options_alter_comment_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
