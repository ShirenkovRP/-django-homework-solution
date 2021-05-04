from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from pprint import pprint

from .models import Badge, Relation, Article


class RelationInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            pprint(form.cleaned_data.get('main'))
            if form.cleaned_data.get('main'):
                count += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')
        print(f'Общее число основных тем {count}')
        if not count:
            raise ValidationError('Укажите основной раздел')
        elif count > 1:
            raise ValidationError('Основным может быть только один раздел')
        else:
            return super().clean()  # вызываем базовый код переопределяемого метода


class RelationInline(admin.TabularInline):
    model = Relation
    formset = RelationInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (RelationInline,)


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    inlines = (RelationInline,)
