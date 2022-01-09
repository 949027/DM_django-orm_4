from django.db import models


class Pokemon(models.Model):
    """Модель покемона"""
    title = models.CharField('Название (ru)', max_length=200)
    title_en = models.CharField('Название (en)', max_length=200, blank=True)
    title_jp = models.CharField('Название (jp)', max_length=200, blank=True)
    image = models.ImageField('Изображение', upload_to='images')
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    attack = models.IntegerField('Атака', null=True, blank=True)
    protection = models.IntegerField('Защита', null=True, blank=True)
    endurance = models.IntegerField('Выносливость', null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Из кого эволюционировал',
        related_name='next_evolution',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    """Появление покемона на карте"""
    appeared_at = models.DateTimeField('Появляется')
    disappeared_at = models.DateTimeField('Исчезает')
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    pokemon = models.ForeignKey(
        Pokemon,
        related_name='pokemons',
        verbose_name='Покемон',
        on_delete=models.CASCADE,
        null=True,
    )
