# Generated by Django 4.2.2 on 2023-06-30 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('tank', 'Танки'), ('healer', 'Хилы'), ('dd', 'ДД'), ('trader', 'Торговцы'), ('guild_master', 'Гилдмастеры'), ('quest_giver', 'Квестгиверы'), ('blacksmith', 'Кузнецы'), ('leatherworker', 'Кожевники'), ('alchemist', 'Зельевары'), ('spellcaster', 'Мастера заклинаний')], max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image1', models.ImageField(blank=True, upload_to='')),
                ('image2', models.ImageField(blank=True, upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.listing')),
            ],
        ),
    ]
