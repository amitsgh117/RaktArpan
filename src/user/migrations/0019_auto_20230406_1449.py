# Generated by Django 3.2.12 on 2023-04-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_user_donor_blood_bank_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='donor_blood_bank_contact',
        ),
        migrations.AddField(
            model_name='user',
            name='donor_blood_bank_contact',
            field=models.ManyToManyField(blank=True, null=True, to='user.User'),
        ),
    ]
