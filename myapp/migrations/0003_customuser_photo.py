# Generated by Django 5.0.6 on 2024-06-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_customuser_birthday_customuser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/img'),
        ),
    ]
