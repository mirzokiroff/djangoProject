# Generated by Django 4.2.2 on 2023-07-14 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrossfitTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='image')),
                ('link', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]