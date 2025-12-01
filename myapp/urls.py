from django.urls import path
from . import views
from django.urls import path
from .views import status_view


urlpatterns = [
    path("status/", status_view, name="api-status"),
    path('hello/', views.hello_view, name='hello'),
    path('welcome/', views.template_view, name='welcome'),
]
