# Generated by Django 3.2.12 on 2023-04-06 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_alter_bloodcamp_description_alter_bloodcamp_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='donor_blood_bank_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
