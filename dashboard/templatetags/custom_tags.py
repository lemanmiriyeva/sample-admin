from django import template

register = template.Library()

@register.filter
def attr(obj, attr_name):
    return getattr(obj, attr_name, '')

@register.filter
def verbose_name(instance):
    return instance.__class__._meta.verbose_name.title()
