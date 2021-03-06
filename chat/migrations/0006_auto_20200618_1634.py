# Generated by Django 3.0.7 on 2020-06-18 16:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0005_auto_20200618_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterUniqueTogether(
            name='message',
            unique_together={('author', 'message')},
        ),
    ]
