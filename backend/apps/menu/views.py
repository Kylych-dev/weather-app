# apps/menu/views.py
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View
from .models import Menu


def menu_view(request):
    menu = Menu.objects.filter(parent__isnull=True).prefetch_related('children')
    return render(
        request,
        'menu/menu.html',
        {'menu': menu}
    )


class NamedUrlView(View):
    def get(self, request, named_url):
        return redirect(reverse(named_url))



# def menu_view(request):
#     print(request, '+++++++++')
#     # menu = Menu.objects.filter(parent__isnull=True).prefetch_related('children')
#     menu_items = Menu.objects.filter(name=menu_name)
#     print(menu, '************')
#     return render(request, 'menu/menu.html', {'menu': menu})
