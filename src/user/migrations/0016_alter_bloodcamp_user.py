# Generated by Django 4.0.3 on 2022-04-09 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_remove_bloodcamp_date_remove_bloodcamp_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodcamp',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]