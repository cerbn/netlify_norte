from django import template

register = template.Library()

@register.filter
def stars_range(value):
    """
    Devuelve un rango de 1 a value, que se puede usar para generar estrellas en la plantilla.
    """
    try:
        value = int(value)
    except ValueError:
        return range(0)
    return range(1, value + 1)
