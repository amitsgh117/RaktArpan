# Generated by Django 3.2.12 on 2023-04-06 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20230406_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='donor_blood_bank_contact',
            field=models.ManyToManyField(blank=True, null=True, related_name='_user_user_donor_blood_bank_contact_+', to='user.User'),
        ),
    ]