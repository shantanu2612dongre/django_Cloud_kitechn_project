# Generated by Django 5.1.1 on 2024-10-11 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restroapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
