from django.urls import path

from app.views import landing, stats, index


urlpatterns = [
    path('', index, name='index'),
    path('landing/<ab_test_arg>/', landing, name='landing'),
    path('stats/', stats, name='stats'),
]
