# Generated by Django 5.1.1 on 2024-10-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('ST', 'Student'), ('CA', 'Career'), ('BU', 'Business')], default='ST', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='YouTubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('category', models.CharField(choices=[('ST', 'Student'), ('CA', 'Career'), ('BU', 'Business')], default='ST', max_length=2)),
            ],
        ),
    ]