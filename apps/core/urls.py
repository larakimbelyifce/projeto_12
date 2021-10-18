from django.urls import path, include
from . import views

app_name = 'core'

# Chamar a view.
urlpatterns = [
    path('', views.home, name='home'),
]
