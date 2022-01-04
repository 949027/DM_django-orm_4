from django.db import models


class Pokemon(models.Model):
    title = models.CharField('Название (ru)', max_length=200)
    title_en = models.CharField('Название (en)', max_length=200, null=True)
    title_jp = models.CharField('Название (jp)',max_length=200, null=True)
    image = models.ImageField('Изображение', upload_to='images', null=True, blank=True)
    level = models.IntegerField('Уровень', null=True)
    health = models.IntegerField('Здоровье', null=True)
    attack = models.IntegerField('Атака', null=True)
    protection = models.IntegerField('Защита', null=True)
    endurance = models.IntegerField('Выносливость', null=True)
    description = models.TextField('Описание', null=True)
    previous_evolution = models.ForeignKey('self', verbose_name='Из кого эволюционировал', related_name='previous', on_delete=models.PROTECT, null=True, blank=True)
    next_evolution = models.ForeignKey('self', verbose_name='В кого эволюционирует',on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    appeared_at = models.DateTimeField('Появляется')
    disappeared_at = models.DateTimeField('Исчезает')
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.PROTECT, null=True)