from django import template

register = template.Library()


@register.filter
def to_tuple(value, arg):
    return (value, arg)