# Generated by Django 2.1.4 on 2018-12-03 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'Media', 'verbose_name_plural': 'Medias'},
        ),
        migrations.AddField(
            model_name='media',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
