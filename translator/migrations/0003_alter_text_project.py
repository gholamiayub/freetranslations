# Generated by Django 3.2.2 on 2022-01-27 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text', to='translator.project'),
        ),
    ]
