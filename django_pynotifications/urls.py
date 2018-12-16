from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('/callback/<str:system>/<str:status>', csrf_exempt(views.callback), name='callback')
]
