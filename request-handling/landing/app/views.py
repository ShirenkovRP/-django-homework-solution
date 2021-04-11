from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    if request.GET.get("from-landing") == "original":
        counter_show["original"] += 1
    elif request.GET.get("from-landing") == "test":
        counter_show["test"] += 1
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    return render(request, 'index.html')


def landing(request, ab_test_arg):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    if ab_test_arg == "original":
        url_html = 'landing.html'

    else:
        url_html = 'landing_alternate.html'
    counter_click["counter_click"] += 1
    return render(request, url_html)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    test_conversion = counter_show["test"] / counter_click["counter_click"]
    original_conversion = counter_show["original"] / counter_click["counter_click"]
    return render(request, 'stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
