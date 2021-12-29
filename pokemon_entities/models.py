from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    level = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    attack = models.IntegerField(null=True)
    protection = models.IntegerField(null=True)
    endurance = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.PROTECT, null=True)