# Generated by Django 4.2.2 on 2023-07-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_subscribe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
