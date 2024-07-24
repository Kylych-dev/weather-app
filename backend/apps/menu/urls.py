from django.urls import path
from .views import (
    menu_view,
    NamedUrlView
)

urlpatterns = [
    path('', menu_view, name='menu_view'),
    path('<str:named_url>/', NamedUrlView.as_view(), name='named_url_view'),


]
