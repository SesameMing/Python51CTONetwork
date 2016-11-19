# Author:Alex Li
from django import template
from django.utils.safestring import mark_safe
from django.template.base import resolve_variable, Node, TemplateSyntaxError

register = template.Library()

@register.filter
def f1(value, arg):
    return value + "666" + arg

@register.simple_tag
def f2(s1,s2,s3, s4):
    return s1 + s2 + s3 + s4

@register.filter
def f3(value):
    if value == 'VVV':
        return True
    return False

@register.simple_tag
def f4(value):
    if value == 'VVV':
        return True
    return False