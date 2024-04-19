# Generated by Django 4.2 on 2024-04-10 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specific_username', models.CharField(default=1, max_length=200)),
                ('friend_code', models.CharField(default=1, max_length=30)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('is_public', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('purpose', models.CharField(blank=True, choices=[('FOR FUN', 'This account exists for fun'), ('FOR BUSINESS', 'This account exists for business reasons'), ('FOR PERSONAL USE', 'This account exists for personal usage'), ('FOR ART', 'This account exists for sharing art'), ('FOR INFLUENCE', 'This account exists for influencer purposes'), ('OTHER', 'This account exists for other reasons')], max_length=200)),
                ('platform', models.CharField(choices=[('TWITTER', 'Twitter'), ('FACEBOOK', 'Facebook'), ('YOUTUBE', 'Youtube'), ('INSTAGRAM', 'Instagram'), ('STEAM', 'Steam'), ('DISCORD', 'Discord'), ('OTHER', 'Another account')], default='NULL', max_length=200)),
            ],
        ),
    ]