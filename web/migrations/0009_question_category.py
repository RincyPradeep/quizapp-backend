# Generated by Django 4.0.4 on 2022-05-23 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.category'),
        ),
    ]
