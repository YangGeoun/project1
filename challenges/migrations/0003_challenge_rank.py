# Generated by Django 4.2.6 on 2023-10-30 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_remove_challenge_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='rank',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
