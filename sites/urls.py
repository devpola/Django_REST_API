from django.urls import path

from .views import SiteAPI

urlpatterns = [
    path('<str:mode>/', SiteAPI.as_view()),
]