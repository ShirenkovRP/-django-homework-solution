from django import template

register = template.Library()

@register.filter()
def change_str_float(world):
    try:
        return float(world)
    except:
        return world