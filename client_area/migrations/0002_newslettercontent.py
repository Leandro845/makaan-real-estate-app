# Generated by Django 5.0.6 on 2024-06-03 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
