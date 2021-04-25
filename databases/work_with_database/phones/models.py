from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля

    name = models.TextField(verbose_name="Наименование")
    price = models.DecimalField(verbose_name="Цена", max_digits=6, decimal_places=0)
    image = models.URLField(verbose_name="Изображение")
    release_date = models.DateField(verbose_name="Дата релиза")
    lte_exists = models.BooleanField(verbose_name="Наличие")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name}'
    # pass
