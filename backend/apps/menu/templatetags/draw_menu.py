# apps/menu/templatetags/menu_tags.py
from django import template
from ..models import Menu

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = Menu.objects.filter(menu_name=menu_name).first()
    if menu:
        menu_items = menu.children.all()
    else:
        menu_items = Menu.objects.none()
    return {
        'menu': menu_items,
        'request': context['request']
    }



# @register.inclusion_tag('menu/menu.html', takes_context=True)
# def draw_menu(context, menu_name):
#     # menu_items = Menu.objects.filter(name=menu_name).prefetch_related('children')
#     menu_items = Menu.objects.filter(name=menu_name).first().children.all()
#     return {
#         'menu': menu_items,
#         'request': context['request']
#     }


# @register.inclusion_tag('menu/menu.html', takes_context=True)
# def draw_menu(context, menu_name):
#
#     menu_items = Menu.objects.filter(parent__isnull=True)
#     print(menu_items, '----------')
#     return {
#         'menu': menu_items,
#         'request': context['request']
#     }

