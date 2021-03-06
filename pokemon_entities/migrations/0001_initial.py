# Generated by Django 3.1.14 on 2022-01-01 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('level', models.IntegerField(null=True)),
                ('health', models.IntegerField(null=True)),
                ('attack', models.IntegerField(null=True)),
                ('protection', models.IntegerField(null=True)),
                ('endurance', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appeared_at', models.DateTimeField()),
                ('disappeared_at', models.DateTimeField()),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('pokemon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pokemon_entities.pokemon')),
            ],
        ),
    ]
