# Generated by Django 3.2.2 on 2022-01-26 09:18

from django.db import migrations, models
import django.db.models.deletion
import martor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250)),
                ('status', models.CharField(choices=[('translating', 'Translating'), ('translated', 'Translated'), ('pending', 'Pending')], default='translating', max_length=15)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=True)),
                ('source_github', models.URLField(unique=True)),
                ('project_github', models.URLField(unique=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('context', martor.models.MartorField()),
                ('slug', models.SlugField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='translator.project')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
