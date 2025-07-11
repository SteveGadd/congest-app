# Generated by Django 4.2.20 on 2025-04-25 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('routing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAreaPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference_type', models.CharField(choices=[('prefer', 'Prefer'), ('avoid', 'Avoid')], max_length=10)),
                ('min_lat', models.DecimalField(decimal_places=7, max_digits=10)),
                ('min_lon', models.DecimalField(decimal_places=7, max_digits=10)),
                ('max_lat', models.DecimalField(decimal_places=7, max_digits=10)),
                ('max_lon', models.DecimalField(decimal_places=7, max_digits=10)),
                ('reason', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='area_preferences', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
