# Generated by Django 5.0.3 on 2024-04-08 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_passwordresettoken'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PasswordResetToken',
        ),
    ]