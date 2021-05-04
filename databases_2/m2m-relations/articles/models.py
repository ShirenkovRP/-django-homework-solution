from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Badge(models.Model):
    title = models.CharField(max_length=32, verbose_name='Тег')
    articles = models.ManyToManyField(Article, related_name='scopes', through='Relation')

    class Meta:
        verbose_name = 'Тематека Статьи'
        verbose_name_plural = 'Тематика Статей'

    def __str__(self):
        return self.title


class Relation(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    main = models.BooleanField(verbose_name='Основной')

    def __str__(self):
        return '{0}_{1}'.format(self.article, self.badge)