from django.urls import path
from myapp.views import form

urlpatterns = [
    path('', form),
]