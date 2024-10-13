# Generated by Django 5.1.2 on 2024-10-13 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='recipient_role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Team Lead'), (3, 'Team Member'), (4, 'Pastorate'), (5, 'Facilitator'), (6, 'Student'), (7, 'Career'), (8, 'Business'), (9, 'Service Team'), (10, 'Management Information System'), (11, 'Household Head'), (12, 'Kbn Career'), (13, 'Kbn Business')]),
        ),
    ]
