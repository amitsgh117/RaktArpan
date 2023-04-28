# Generated by Django 3.2.12 on 2023-04-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_donationcertificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationcertificate',
            name='signature',
            field=models.CharField(default='RakTarpan', max_length=30),
        ),
        migrations.AlterField(
            model_name='donationcertificate',
            name='date',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
