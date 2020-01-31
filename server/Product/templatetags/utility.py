from django import template

register = template.Library()

@register.simple_tag
def get_value_by_key(source, key):
    return source.get(key) if isinstance(source, dict) else source


# @register.filter(name='not_null')
# def get_not_empty(source):
#     return (itm for itm in source if itm)


@register.filter(name='not_null')
def not_empty(source):
    return source if source else "-"

@register.filter(name="index")
def index(indexable, i):
    try:
        return indexable[i]
    except IndexError:
        return None
