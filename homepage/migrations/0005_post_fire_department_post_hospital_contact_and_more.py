# Generated by Django 4.0.1 on 2022-01-10 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fire_department',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hospital_contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='security_department',
            field=models.IntegerField(null=True),
        ),
    ]
