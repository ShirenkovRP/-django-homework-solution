from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    if sort == 'name':
        elements_db = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        elements_db = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        elements_db = Phone.objects.all().order_by('-price')
    else:
        elements_db = Phone.objects.all()

    context = {"phones": elements_db}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    element_db = Phone.objects.filter(slug=slug)
    context = {'telephone': element_db}
    return render(request, template, context)
